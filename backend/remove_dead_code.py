with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _old_scan_sql_injection_unused(source, filename):
    import re as _re8
    lines = source.split(chr(10))
    issues = []
    patterns = [(r"(?i)(execute|executemany)\\s*\\(.*[+%]", "String concatenation/formatting in SQL query - use parameterized queries instead"), (r"(?i)(SELECT|INSERT|UPDATE|DELETE).*[+].*(request|input|user|param|arg|var)", "SQL string built with concatenation - injection risk"), (r"(?i)(query|sql)\\s*=\\s*.*%\\s*[a-zA-Z]", "SQL built with string formatting - injection risk"), (r"(?i)\\.format\\s*\\(.*(SELECT|INSERT|UPDATE|DELETE|WHERE)", "SQL built with .format() - injection risk"), (r"(?i)f[\\"\\x27].*(SELECT|INSERT|UPDATE|DELETE|WHERE).*\\{", "SQL built with f-string variables - injection risk")]
    for i, line in enumerate(lines):
        for pat, msg in patterns:
            if _re8.search(pat, line):
                issues.append({"line": i+1, "code": line.strip()[:120], "issue": msg, "severity": "High"})
                break
    safe = bool(_re8.search(r"(?i)(execute\\s*\\([^)]*,\\s*[\\(\\[])|%s|\\?)", source)) and len(issues) == 0
    return {"sqli_safe": len(issues) == 0, "sqli_issues": issues, "sqli_summary": (str(len(issues)) + " potential SQL injection risk(s) found - review these lines") if issues else "No obvious SQL injection patterns detected in this file", "sqli_disclaimer": "Detects common SQL injection patterns (string concatenation/formatting in queries). Pattern-based - always confirm with a security review and use parameterized queries."}

'''
new = ""

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("DEAD CODE REMOVED SUCCESSFULLY")
else:
    print("FAILED - will leave dead code in place, not critical")