with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''(r"(?i)\\b(risk[_\\s]?score|risk[_\\s]?rating|risk[_\\s]?category)\\b", "Customer risk scoring", "KYC", "Risk-scoring rules affect compliance decisions - review carefully."),'''
new = old + '''
    (r"(?i)\\b(FATF|OFAC|FinCEN|\\bFIU\\b)\\b", "Regulatory body reference", "AML", "Verify regulatory-body logic is preserved exactly."),
    (r"(?i)\\b(beneficial[_\\s]?owner|\\bUBO\\b)\\b", "Beneficial ownership check", "KYC", "Verify beneficial-ownership verification logic preserved."),
    (r"(?i)\\b(name[_\\s]?screening|fuzzy[_\\s]?match)\\b", "Name screening logic", "AML", "Verify name-screening/matching logic preserved."),
    (r"(?i)\\b(customer[_\\s]?onboarding|onboarding[_\\s]?process)\\b", "Customer onboarding", "KYC", "Verify onboarding compliance checks preserved."),
    (r"(?i)\\b(dormant[_\\s]?account|inactive[_\\s]?account)\\b", "Dormant account logic", "AML", "Dormant-account rules often have compliance implications."),'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")