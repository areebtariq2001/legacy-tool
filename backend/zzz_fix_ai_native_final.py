with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    # 3. Hardcoded values / config (blocks flexible AI integration)
    import re as _re
    if _re.search(r"(?i)(localhost|127\\.0\\.0\\.1|hardcoded|password\\s*=\\s*[\\x22\\x27]|[\\w-]*password[\\w-]*\\s+PIC\\s+X.*VALUE\\s+[\\x22\\x27])", source):
        score -= 15
        findings.append({"issue": "Hardcoded config/credentials - blocks flexible deployment in AI environments", "impact": "Medium"})
    # 4. print statements instead of logging (not observable for AI pipelines)
    if _re.search(r"(?m)^\\s*print\\s*\\(", source):
        score -= 10
        findings.append({"issue": "Uses print() instead of logging - AI pipelines need structured logs", "impact": "Low"})'''

new = '''    # 3. Hardcoded values / config (blocks flexible AI integration)
    _re = re
    if _re.search(r"(?i)(localhost|127\\.0\\.0\\.1|password\\s*=\\s*[\\x22\\x27]|[\\w-]*password[\\w-]*\\s+PIC\\s+X.*VALUE\\s+[\\x22\\x27])", source):
        score -= 15
        findings.append({"issue": "Hardcoded config/credentials - blocks flexible deployment in AI environments", "impact": "Medium"})
    # 4. print statements instead of logging (not observable for AI pipelines) - Python only
    if filename.lower().endswith(".py") and _re.search(r"(?m)^\\s*print\\s*\\(", source):
        score -= 10
        findings.append({"issue": "Uses print() instead of logging - AI pipelines need structured logs", "impact": "Low"})'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")