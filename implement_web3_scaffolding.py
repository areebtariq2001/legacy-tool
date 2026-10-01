main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.get("/blockchain-status")'''

new = '''class BlockchainApproval:
    """
    Phase 3/4 scaffolding: a connector point for a REAL external blockchain
    network (Ethereum testnet/mainnet via web3.py, or similar), kept
    deliberately inactive-by-default. This is honest scaffolding, not a
    working integration - it requires the operator to provide their own
    ETHEREUM_RPC_URL (e.g. a free Infura/Alchemy project) and a funded wallet
    with a deployed StarBuildApproval smart contract before it does anything.
    Without that configuration, every method here safely no-ops and returns
    a clear "not configured" status rather than failing or pretending to
    have recorded something on-chain that it did not.
    """
    def __init__(self):
        self.enabled = False
        self.w3 = None
        rpc_url = os.environ.get("ETHEREUM_RPC_URL", "")
        if rpc_url:
            try:
                from web3 import Web3
                self.w3 = Web3(Web3.HTTPProvider(rpc_url))
                self.enabled = self.w3.is_connected()
            except Exception:
                self.enabled = False

    def status(self):
        return {
            "enabled": self.enabled,
            "note": "Distributed-ledger recording is not active. Set ETHEREUM_RPC_URL (and deploy a contract) to enable this in the future - see Phase 3/4 of the blockchain roadmap for the planned Solidity contract and web3.py wiring." if not self.enabled else "Connected to configured RPC endpoint."
        }

    def record_on_chain(self, approval_data):
        if not self.enabled:
            return {"recorded": False, "reason": "Distributed ledger not configured (ETHEREUM_RPC_URL not set or unreachable) - this is expected in the current deployment and is not an error."}
        return {"recorded": False, "reason": "RPC connection is available, but contract interaction is not yet implemented - this remains future work."}


blockchain_approval = BlockchainApproval()


@app.get("/distributed-ledger-status")
async def distributed_ledger_status_endpoint():
    return blockchain_approval.status()


@app.get("/blockchain-status")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("WEB3-SCAFFOLDING-ADDED")
else:
    print("FAILED - count was:", count)