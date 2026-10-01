main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Add _head_hash to __init__
old1 = '''    def __init__(self):
        self.chain = []
        self._lock = threading.Lock()
        self._next_index = 0
        self._total_blocks_created = 0
        self._create_genesis_block()'''
new1 = '''    def __init__(self):
        self.chain = []
        self._lock = threading.Lock()
        self._next_index = 0
        self._total_blocks_created = 0
        self._head_hash = None  # tracks the hash of the most-recently-added block, independent of
        # the chain list itself, so verify_chain can detect if the most recent block(s) were
        # deleted from the chain - a truncated-but-otherwise-internally-consistent chain would
        # otherwise report as fully valid, since nothing else checks against an external anchor
        self._create_genesis_block()'''
results["1_init_head_hash"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Update _head_hash in genesis block creation
old2 = '''        self.chain.append(genesis)
        self._next_index += 1
        self._total_blocks_created += 1'''
new2 = '''        self.chain.append(genesis)
        self._next_index += 1
        self._total_blocks_created += 1
        self._head_hash = genesis.hash'''
results["2_genesis_head_hash"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Update _head_hash in add_block
old3 = '''            self.chain.append(new_block)
            self._next_index += 1
            self._total_blocks_created += 1
            del self.chain[:-2000]
            return new_block'''
new3 = '''            self.chain.append(new_block)
            self._next_index += 1
            self._total_blocks_created += 1
            self._head_hash = new_block.hash
            del self.chain[:-2000]
            return new_block'''
results["3_addblock_head_hash"] = content.count(old3)
content = content.replace(old3, new3, 1)

# Add head-hash check at the end of verify_chain
old4 = '''            if not current.hash.startswith(_difficulty_prefix):
                return False, current.index
            if current.previous_hash != previous.hash:
                return False, current.index
        return True, None'''
new4 = '''            if not current.hash.startswith(_difficulty_prefix):
                return False, current.index
            if current.previous_hash != previous.hash:
                return False, current.index
        if self._head_hash is not None and len(self.chain) > 0 and self.chain[-1].hash != self._head_hash:
            return False, "chain truncated - most recent block(s) missing (head hash mismatch)"
        return True, None'''
results["4_verify_head_hash"] = content.count(old4)
content = content.replace(old4, new4, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXHEADANCHOR-DONE")