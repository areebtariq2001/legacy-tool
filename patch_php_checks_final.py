with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        (r'\\bsql_regcase\\b', "sql_regcase() found - removed in PHP 7"),
    ]'''

new = '''        (r'\\bsql_regcase\\b', "sql_regcase() found - removed in PHP 7"),
        (r'\\bmoney_format\\s*\\(', "money_format() found - removed in PHP 8.0, use NumberFormatter instead"),
        (r'class\\s+(\\w+)\\s*\\{[^}]*?function\\s+\\1\\s*\\(', "PHP 4-style constructor (method name matches class name) found - removed in PHP 8, use __construct() instead"),
    ]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")