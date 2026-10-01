main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: add persistent counters to __init__
old1 = '''    def __init__(self):
        self.chain = []
        self._lock = threading.Lock()
        self._create_genesis_block()'''
new1 = '''    def __init__(self):
        self.chain = []
        self._lock = threading.Lock()
        self._next_index = 0
        self._total_blocks_created = 0
        self._create_genesis_block()'''
results["1_init_counters"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: genesis block uses and increments the persistent counter
old2 = '''    def _create_genesis_block(self):
        genesis = AuditBlock(0, time.time(), "GENESIS", "system", "system", "0.0.0.0", "StarBuild Audit Chain Initialized", "0" * 64)
        genesis.mine(difficulty=2)
        self.chain.append(genesis)'''
new2 = '''    def _create_genesis_block(self):
        genesis = AuditBlock(self._next_index, time.time(), "GENESIS", "system", "system", "0.0.0.0", "StarBuild Audit Chain Initialized", "0" * 64)
        genesis.mine(difficulty=2)
        self.chain.append(genesis)
        self._next_index += 1
        self._total_blocks_created += 1'''
results["2_genesis_counter"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: add_block uses the persistent counter instead of len(self.chain), so index stays unique even after old blocks are trimmed
old3 = '''    def add_block(self, action, filename, user_email, ip, result):
        with self._lock:
            prev_block = self.chain[-1]
            new_block = AuditBlock(len(self.chain), time.time(), action, filename, user_email, ip, str(result)[:200], prev_block.hash)
            new_block.mine(difficulty=2)
            self.chain.append(new_block)
            del self.chain[:-2000]
            return new_block'''
new3 = '''    def add_block(self, action, filename, user_email, ip, result):
        with self._lock:
            prev_block = self.chain[-1]
            new_block = AuditBlock(self._next_index, time.time(), action, filename, user_email, ip, str(result)[:200], prev_block.hash)
            new_block.mine(difficulty=2)
            self.chain.append(new_block)
            self._next_index += 1
            self._total_blocks_created += 1
            del self.chain[:-2000]
            return new_block'''
results["3_addblock_counter"] = content.count(old3)
content = content.replace(old3, new3, 1)

# Fix 4: verify_chain now verifies the genesis/oldest-surviving block's own hash and proof-of-work,
# and checks proof-of-work difficulty for every block, not just the hash-chain linkage
old4 = '''    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                return False, current.index
            if current.previous_hash != previous.hash:
                return False, current.index
        return True, None'''
new4 = '''    def verify_chain(self):
        _difficulty_prefix = "00"
        if len(self.chain) > 0:
            _first = self.chain[0]
            if _first.hash != _first.compute_hash():
                return False, _first.index
            if not _first.hash.startswith(_difficulty_prefix):
                return False, _first.index
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                return False, current.index
            if not current.hash.startswith(_difficulty_prefix):
                return False, current.index
            if current.previous_hash != previous.hash:
                return False, current.index
        return True, None'''
results["4_verify_chain"] = content.count(old4)
content = content.replace(old4, new4, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXBLOCKCHAIN-DONE")