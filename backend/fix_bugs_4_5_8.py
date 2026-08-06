with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old4 = '''        write_audit_log("scan-sensitive", file.filename, "findings=" + str(result.get("total_findings", 0)))'''
new4 = '''        write_audit_log("scan-sensitive", file.filename, f"findings={result.get('total_findings', 0)}")'''

old5 = '''(r"(?i)\\b(currency|exchange[_\\s]?rate|forex|decimal|round)\\b", "Currency/precision logic",'''
new5 = '''(r"(?i)\\b(currency|exchange[_\\s]?rate|forex|round\\(.*,\\s*2\\))\\b", "Currency/precision logic",'''

old8 = '''(r"(?i)\\b(loan|disburse|repayment|loan.?default)\\b", "Loan processing"'''
new8 = '''(r"(?i)\\b(AML|KYC|FATF|sanctions[_\\s]?list|watchlist)\\b", "AML/KYC compliance logic", "Verify compliance logic preserved."),
    (r"(?i)\\b(SBP|Basel[_\\s]?(I{1,3}|1|2|3)|PCI.?DSS|GDPR|IFRS)\\b", "Regulatory compliance reference", "Ensure regulatory rules unchanged."),
    (r"(?i)\\b(audit[_\\s]?trail|audit[_\\s]?log)\\b", "Audit trail logic", "Verify audit logging preserved exactly."),
    (r"(?i)\\b(encryption|decrypt|cipher|key[_\\s]?store)\\b", "Encryption logic", "Verify cryptographic operations unchanged."),
    (r"(?i)\\b(loan|disburse|repayment|loan.?default)\\b", "Loan processing"'''

count4 = content.count(old4)
count5 = content.count(old5)
count8 = content.count(old8)
print("Bug-4 occurrences:", count4)
print("Bug-5 occurrences:", count5)
print("Bug-8 occurrences:", count8)

if count4 == 1:
    content = content.replace(old4, new4, 1)
    print("Bug-4 PATCHED")
if count5 == 1:
    content = content.replace(old5, new5, 1)
    print("Bug-5 PATCHED")
if count8 == 1:
    content = content.replace(old8, new8, 1)
    print("Bug-8 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")