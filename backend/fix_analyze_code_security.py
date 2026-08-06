with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    if parse_failed:
        issues.insert(0, "Could not fully parse with Python's AST (likely Python 2-only syntax) - showing pattern-based findings below; function/class detection may be incomplete.")
    return {"functions": functions, "classes": classes, "imports": imports, "issues": issues, "ast_parse_failed": parse_failed}'''

new = '''    try:
        _sqli_result = scan_sql_injection(source, "file.py")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    try:
        _sens_result = scan_sensitive_data(source)
        for _sens_finding in _sens_result.get("findings", []):
            if _sens_finding["severity"] in ("High", "Critical"):
                issues.append(_sens_finding["issue"] + " (line(s): " + _sens_finding.get("lines", "?") + ")")
    except Exception:
        pass
    if parse_failed:
        issues.insert(0, "Could not fully parse with Python's AST (likely Python 2-only syntax) - showing pattern-based findings below; function/class detection may be incomplete.")
    return {"functions": functions, "classes": classes, "imports": imports, "issues": issues, "ast_parse_failed": parse_failed}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")