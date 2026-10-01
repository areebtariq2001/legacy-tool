main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old1 = '''def write_audit_log(action, filename, result_summary):
    global _audit_log_failure_count
    result_summary = safe_log_message(result_summary)
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = _get_db_connection()
        if conn:
            cur = None
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO usage_log (action, filename, result_summary) VALUES (%s, %s, %s)", (action, filename, result_summary))
                conn.commit()
                return
            except Exception:
                pass
            finally:
                if cur:
                    cur.close()
                conn.close()
        with _stats_lock:
            _in_memory_audit_log.insert(0, {"timestamp": timestamp, "action": action, "file": filename, "result": result_summary})
            del _in_memory_audit_log[50:]
    except Exception:
        _audit_log_failure_count += 1'''

new1 = '''class AuditBlock:
    def __init__(self, index, timestamp, action, filename, user_email, ip_address, result_summary, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.action = action
        self.filename = filename
        self.user_email = user_email
        self.ip_address = ip_address
        self.result_summary = result_summary
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = ""

    def compute_hash(self):
        block_data = {
            "index": self.index, "timestamp": self.timestamp, "action": self.action,
            "filename": self.filename, "user_email": self.user_email, "ip_address": self.ip_address,
            "result_summary": self.result_summary, "previous_hash": self.previous_hash, "nonce": self.nonce,
        }
        return hashlib.sha256(json.dumps(block_data, sort_keys=True).encode()).hexdigest()

    def mine(self, difficulty=2):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.compute_hash()


class StarBuildBlockchain:
    """
    NOTE: this is a single-process, in-memory hash chain with a proof-of-work
    step for demonstration purposes - not a distributed/decentralized blockchain
    (no multiple nodes, no network consensus). Its genuine security property is
    identical to the hash-chained _security_log elsewhere in this file: any edit
    to a past block changes that block's hash, which breaks the chain link to
    every block after it, making tampering detectable via verify_chain(). Like
    the in-memory security log, this chain resets on server restart.
    """
    def __init__(self):
        self.chain = []
        self._lock = threading.Lock()
        self._create_genesis_block()

    def _create_genesis_block(self):
        genesis = AuditBlock(0, time.time(), "GENESIS", "system", "system", "0.0.0.0", "StarBuild Audit Chain Initialized", "0" * 64)
        genesis.mine(difficulty=2)
        self.chain.append(genesis)

    def add_block(self, action, filename, user_email, ip, result):
        with self._lock:
            prev_block = self.chain[-1]
            new_block = AuditBlock(len(self.chain), time.time(), action, filename, user_email, ip, str(result)[:200], prev_block.hash)
            new_block.mine(difficulty=2)
            self.chain.append(new_block)
            del self.chain[:-2000]
            return new_block

    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.compute_hash():
                return False, current.index
            if current.previous_hash != previous.hash:
                return False, current.index
        return True, None

    def get_summary(self):
        is_valid, tampered_at = self.verify_chain()
        return {
            "total_blocks": len(self.chain),
            "chain_valid": is_valid,
            "tampered_block": tampered_at,
            "genesis_hash": self.chain[0].hash,
            "latest_hash": self.chain[-1].hash,
            "integrity_status": "VERIFIED" if is_valid else f"TAMPERED at block {tampered_at}",
            "disclaimer": "This is a single-process, in-memory hash chain (with proof-of-work for demonstration), not a distributed blockchain. It provides the same tamper-evidence property as a real blockchain's linked-hash structure, but resets on server restart and has no independent network of validators."
        }


audit_blockchain = StarBuildBlockchain()


def write_audit_log(action, filename, result_summary):
    global _audit_log_failure_count
    result_summary = safe_log_message(result_summary)
    try:
        audit_blockchain.add_block(action, filename, "anonymous", "unknown", result_summary)
    except Exception:
        pass
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = _get_db_connection()
        if conn:
            cur = None
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO usage_log (action, filename, result_summary) VALUES (%s, %s, %s)", (action, filename, result_summary))
                conn.commit()
                return
            except Exception:
                pass
            finally:
                if cur:
                    cur.close()
                conn.close()
        with _stats_lock:
            _in_memory_audit_log.insert(0, {"timestamp": timestamp, "action": action, "file": filename, "result": result_summary})
            del _in_memory_audit_log[50:]
    except Exception:
        _audit_log_failure_count += 1'''

results["1_blockchain_and_wiring"] = content.count(old1)
content = content.replace(old1, new1, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("BLOCKCHAIN-IMPLEMENTED")