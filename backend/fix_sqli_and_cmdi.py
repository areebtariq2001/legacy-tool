with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''checks = [("execute", "+", "String concatenation inside execute() - SQL injection risk"), ("execute", "%", "String formatting inside execute() - SQL injection risk"), ("execute", ".format", "format() inside execute() - SQL injection risk"), ("SELECT", "+", "SQL SELECT built with + concatenation - injection risk"), ("INSERT", "+", "SQL INSERT built with + concatenation - injection risk"), ("UPDATE", "+", "SQL UPDATE built with + concatenation - injection risk"), ("DELETE", "+", "SQL DELETE built with + concatenation - injection risk"), ("WHERE", "+", "SQL WHERE clause built with + concatenation - injection risk")]'''

new = '''checks = [("execute", "+", "String concatenation inside execute() - SQL injection risk"), ("execute", "%", "String formatting inside execute() - SQL injection risk"), ("execute", ".format", "format() inside execute() - SQL injection risk"), ("SELECT", "+", "SQL SELECT built with + concatenation - injection risk"), ("INSERT", "+", "SQL INSERT built with + concatenation - injection risk"), ("UPDATE", "+", "SQL UPDATE built with + concatenation - injection risk"), ("DELETE", "+", "SQL DELETE built with + concatenation - injection risk"), ("WHERE", "+", "SQL WHERE clause built with + concatenation - injection risk"), ("SELECT", "%", "SQL SELECT built with % string formatting - injection risk"), ("INSERT", "%", "SQL INSERT built with % string formatting - injection risk"), ("UPDATE", "%", "SQL UPDATE built with % string formatting - injection risk"), ("DELETE", "%", "SQL DELETE built with % string formatting - injection risk"), ("WHERE", "%", "SQL WHERE clause built with % string formatting - injection risk"), ("SELECT", ".format", "SQL SELECT built with .format() - injection risk"), ("WHERE", ".format", "SQL WHERE clause built with .format() - injection risk")]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")