import main
import hashlib
import json
from fastapi.testclient import TestClient

client = TestClient(main.app)

with open("testcert_result.txt", "w", encoding="utf-8") as out:
    # Test 1: Unauthenticated request should get 401
    r1 = client.post("/issue-migration-certificate", json={"filename": "test.py", "decision": "Approved"})
    out.write("Test-1 (no-auth): status=" + str(r1.status_code) + " (expect 401)\n\n")

    # Test 2: Genuine certificate issued via the real function should verify correctly
    cert = main.cert_manager.issue(filename="test2.py", original_hash="abc", migrated_hash="def", confidence=100, reviewer_email="real@test.com", approved=True)
    verify_result = main.cert_manager.verify(cert["certificate_id"])
    out.write("Test-2 (genuine-cert-verify): valid=" + str(verify_result.get("valid")) + " (expect True)\n\n")

    # Test 3: Attacker tries to FORGE a certificate using the OLD vulnerable plain-SHA256 approach
    forged_cert = {
        "certificate_id": "STARBUILD-FORGED123456",
        "issued_at": "2026-01-01T00:00:00",
        "filename": "malicious.py",
        "original_code_hash": "fake",
        "migrated_code_hash": "fake",
        "confidence_score": 100,
        "approved_by": "attacker",
        "approval_status": "APPROVED",
        "blockchain_block": 0,
        "chain_hash_at_issuance": "fake",
    }
    forged_signature = hashlib.sha256(json.dumps(forged_cert, sort_keys=True).encode()).hexdigest()
    forged_cert["certificate_signature"] = forged_signature
    main.cert_manager.certificates["STARBUILD-FORGED123456"] = forged_cert
    forge_verify_result = main.cert_manager.verify("STARBUILD-FORGED123456")
    out.write("Test-3 (forged-cert-with-old-plain-sha256): valid=" + str(forge_verify_result.get("valid")) + " reason=" + str(forge_verify_result.get("reason")) + " (expect valid=False, tampered)\n")
print("TESTCERT-DONE")