with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''(r"(?i)(ssn|social_security)", "Social security reference"), (r"(?i)(account_number|acct_no|iban|routing)", "Bank account field")]'''
new = '''(r"(?i)(ssn|social_security)\\s*=\\s*[\\"\\x27][^\\"\\x27]{2,}[\\"\\x27]", "Social security reference (hardcoded value)"), (r"(?i)(account_number|acct_no|iban|routing)\\s*=\\s*[\\"\\x27][^\\"\\x27]{2,}[\\"\\x27]", "Bank account field (hardcoded value)")]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")