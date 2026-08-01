with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''    for pattern, msg in java_checks:
        if re.search(pattern, source):
            issues.append(msg)
    classes = re.findall(r"(?:public|private|protected)?\\s*class\\s+(\\w+)", source)'''

new1 = '''    for pattern, msg in java_checks:
        if re.search(pattern, source):
            issues.append(msg)
    if re.search(r"(?i)(password|passwd|pwd|pass|api_key|apikey|secret)\\s*=\\s*[\\x22\\x27][^\\x22\\x27]{3,}[\\x22\\x27]", source):
        issues.append("Hardcoded password/credential found - move to environment variable")
    try:
        _sqli_result = scan_sql_injection(source, "file.java")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    classes = re.findall(r"(?:public|private|protected)?\\s*class\\s+(\\w+)", source)'''

old2 = '''    for pattern, msg in cobol_checks:
        if pattern in source:
            issues.append(msg)
    return {"issues": issues}'''

new2 = '''    for pattern, msg in cobol_checks:
        if pattern in source:
            issues.append(msg)
    if re.search(r"(?i)(password|passwd|pwd|pass|api-key|apikey|secret)[\\w-]*\\s+PIC\\s+X.*VALUE\\s+[\\x22\\x27][^\\x22\\x27]{2,}[\\x22\\x27]", source):
        issues.append("Hardcoded password/credential found in COBOL VALUE clause - move to environment/config")
    try:
        _sqli_result = scan_sql_injection(source, "file.cbl")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    return {"issues": issues}'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Java fix occurrences:", count1)
print("COBOL fix occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Java PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("COBOL PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")