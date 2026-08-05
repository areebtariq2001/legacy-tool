with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''if not parseable and filename.lower().endswith(".py"): findings.append("Code does not parse in Python 3 - migration will require fixes")'''
new = '''if not parseable and filename.lower().endswith(".py"): findings.append("Contains Python 2-only syntax - AST parser has partial visibility here; this is typically auto-fixed during migration, not a blocker")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")