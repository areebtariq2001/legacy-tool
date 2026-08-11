with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    _re = re
    if _re.search(r"(?i)(localhost|127\\.0\\.0\\.1|password\\s*=\\s*[\\x22\\x27]|[\\w-]*password[\\w-]*\\s+PIC\\s+X.*VALUE\\s+[\\x22\\x27])", source):
        score -= 15
        findings.append({"issue": "Hardcoded config/credentials - blocks flexible deployment in AI environments", "impact": "Medium"})'''

new = '''    _re = re
    _is_test_file = bool(_re.search(r"(?i)(test|spec)", filename))
    if _re.search(r"(?i)(password\\s*=\\s*[\\x22\\x27]|[\\w-]*password[\\w-]*\\s+PIC\\s+X.*VALUE\\s+[\\x22\\x27])", source):
        score -= 15
        findings.append({"issue": "Hardcoded config/credentials - blocks flexible deployment in AI environments", "impact": "Medium"})
    elif not _is_test_file and _re.search(r"(?i)(localhost|127\\.0\\.0\\.1)", source):
        score -= 10
        findings.append({"issue": "Hardcoded localhost/IP address - blocks flexible deployment in AI environments", "impact": "Low"})'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")