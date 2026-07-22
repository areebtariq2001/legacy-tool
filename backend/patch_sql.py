import re

with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    if filename.lower().endswith(".php"):
        checks += [("SELECT", " . ", "SQL SELECT built with . (PHP) concatenation - injection risk"), ("INSERT", " . ", "SQL INSERT built with . (PHP) concatenation - injection risk"), ("UPDATE", " . ", "SQL UPDATE built with . (PHP) concatenation - injection risk"), ("DELETE", " . ", "SQL DELETE built with . (PHP) concatenation - injection risk"), ("WHERE", " . ", "SQL WHERE clause built with . (PHP) concatenation - injection risk")]'''

new = old + '''
    cobol_exec_sql = _sq.search(r"(?is)EXEC\\s+SQL.*?WHERE.*?=\\s*['\\"][^'\\"]+['\\"].*?END-EXEC", source)
    if cobol_exec_sql:
        issues.append({"line": source[:cobol_exec_sql.start()].count(chr(10))+1, "code": cobol_exec_sql.group()[:120].replace(chr(10), " "), "issue": "COBOL embedded SQL (EXEC SQL) with hardcoded literal in WHERE clause - use a host variable instead", "severity": "High"})'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")