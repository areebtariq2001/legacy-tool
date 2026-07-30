with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_line = 213
idx = target_line - 1

print("Line 213 content:", repr(lines[idx]))

insert_code = '''
DEBT_RULES_COMPILED = [(re.compile(p), l, m) for p, l, m in DEBT_RULES]
JAVA_DEBT_RULES_COMPILED = [
    (re.compile(r"\\bVector\\b"), "Vector (legacy collection)", 5),
    (re.compile(r"\\bHashtable\\b"), "Hashtable (legacy collection)", 5),
    (re.compile(r"\\bStringBuffer\\b"), "StringBuffer (use StringBuilder)", 5),
    (re.compile(r"System\\.out\\.println"), "System.out.println (use logging framework)", 5),
]
PHP_DEBT_RULES_COMPILED = [
    (re.compile(r"\\bmysql_\\w+\\b"), "mysql_* (deprecated, use mysqli/PDO)", 10),
    (re.compile(r"\\beach\\("), "each() (removed in PHP 8)", 5),
    (re.compile(r"\\bcreate_function\\b"), "create_function() (removed in PHP 8)", 5),
]
COBOL_DEBT_RULES_COMPILED = [
    (re.compile(r"(?i)GO\\s+TO"), "GO TO (unstructured control flow)", 10),
    (re.compile(r"(?i)REDEFINES"), "REDEFINES (implicit type reinterpretation, hard to migrate)", 15),
    (re.compile(r"(?i)ALTER\\s"), "ALTER statement (deprecated, dynamic GOTO)", 20),
]
'''

lines.insert(idx + 1, insert_code)

with open("main.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("INSERTED SUCCESSFULLY")