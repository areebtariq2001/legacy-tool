with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''reasons.append("Code does not parse in Python 3 - will require fixes before migration")'''
new = '''reasons.append("Contains Python 2-only syntax (e.g. print statement without parentheses) - the AST parser has partial visibility here; pattern-based analysis is used as a fallback. This is typically auto-fixed during migration, not a blocker.")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")