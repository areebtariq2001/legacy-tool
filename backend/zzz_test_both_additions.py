import main

# Test 1: PII evidence
test_pii = 'password = "secret123"'
r1 = main.detect_pii(test_pii, "test.py")
print("PII evidence:", r1["pii_findings"][0].get("evidence") if r1["pii_findings"] else "NONE")

# Test 2: Compliance breakdown
test_exec = '''def log_transaction(txn):
    write_audit_log("txn", txn)
    if check_authorization(txn):
        return True'''
r2 = main.generate_executive_report(test_exec, "test.py")
print("Compliance readiness:", r2.get("exec_compliance_readiness"))