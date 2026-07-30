with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    active_rules = list(DEBT_RULES)
    if filename.lower().endswith(".java"):
        active_rules += [(r"\\bVector\\b", "Vector (legacy collection)", 5), (r"\\bHashtable\\b", "Hashtable (legacy collection)", 5), (r"\\bStringBuffer\\b", "StringBuffer (use StringBuilder)", 5), (r"System\\.out\\.println", "System.out.println (use logging framework)", 5)]
    elif filename.lower().endswith(".php"):
        active_rules += [(r"\\bmysql_\\w+\\b", "mysql_* (deprecated, use mysqli/PDO)", 10), (r"\\beach\\(", "each() (removed in PHP 8)", 5), (r"\\bcreate_function\\b", "create_function() (removed in PHP 8)", 5)]
    elif filename.lower().endswith(".cbl") or filename.lower().endswith(".cob"):
        active_rules += [(r"(?i)GO\\s+TO", "GO TO (unstructured control flow)", 10), (r"(?i)REDEFINES", "REDEFINES (implicit type reinterpretation, hard to migrate)", 15), (r"(?i)ALTER\\s", "ALTER statement (deprecated, dynamic GOTO)", 20)]
    for pattern, label, mins in active_rules:
        matches = re.findall(pattern, source)'''

new = '''    active_rules = list(DEBT_RULES_COMPILED)
    if filename.lower().endswith(".java"):
        active_rules += JAVA_DEBT_RULES_COMPILED
    elif filename.lower().endswith(".php"):
        active_rules += PHP_DEBT_RULES_COMPILED
    elif filename.lower().endswith(".cbl") or filename.lower().endswith(".cob"):
        active_rules += COBOL_DEBT_RULES_COMPILED
    for pattern, label, mins in active_rules:
        matches = pattern.findall(source)'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe, no changes made")