with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    for pattern, repl, label in rules:
        if re.search(pattern, migrated):
            migrated = re.sub(pattern, repl, migrated)
            changes.append(label)
    review_rules = ['''

new = '''    for pattern, repl, label in rules:
        _new_migrated = re.sub(pattern, repl, migrated)
        if _new_migrated != migrated:
            migrated = _new_migrated
            changes.append(label)
    review_rules = ['''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")