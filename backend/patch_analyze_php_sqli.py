with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    for pattern, msg in php_checks:
        if re.search(pattern, source):
            issues.append(msg)
    return {"issues": issues}

def migrate_php(source):'''

new = '''    for pattern, msg in php_checks:
        if re.search(pattern, source):
            issues.append(msg)
    try:
        _sqli_result = scan_sql_injection(source, "file.php")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    return {"issues": issues}

def migrate_php(source):'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")