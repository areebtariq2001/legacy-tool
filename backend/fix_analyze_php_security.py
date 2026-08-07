with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    try:
        _sqli_result = scan_sql_injection(source, "file.php")
        for _sqli_issue in _sqli_result.get("sqli_issues", []):
            issues.append("SQL injection risk (line " + str(_sqli_issue["line"]) + "): " + _sqli_issue["issue"])
    except Exception:
        pass
    _php_funcs = list(dict.fromkeys(re.findall(r"function\\s+(\\w+)\\s*\\(", source)))
    _php_classes = list(dict.fromkeys(re.findall(r"\\bclass\\s+(\\w+)", source)))
    return {"issues": issues, "classes": _php_classes, "methods": _php_funcs[:20], "total_methods": len(_php_funcs), "methods_truncated": len(_php_funcs) > 20, "php_summary": str(len(_php_classes)) + " class(es), " + str(len(_php_funcs)) + " function(s) found"}'''

new = '''    try:
        _sqli_result = scan_sql_injection(source, "file.php")
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
    _php_funcs = list(dict.fromkeys(re.findall(r"function\\s+(\\w+)\\s*\\(", source)))
    _php_classes = list(dict.fromkeys(re.findall(r"\\bclass\\s+(\\w+)", source)))
    return {"issues": issues, "classes": _php_classes, "methods": _php_funcs[:20], "total_methods": len(_php_funcs), "methods_truncated": len(_php_funcs) > 20, "php_summary": str(len(_php_classes)) + " class(es), " + str(len(_php_funcs)) + " function(s) found"}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")