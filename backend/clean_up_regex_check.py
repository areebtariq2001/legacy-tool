with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    for pattern, msg in cobol_checks:
        if re.search(r'\\b' + pattern.replace(chr(92)+"b","") if False else pattern, source, re.IGNORECASE):
            issues.append(msg)'''

new = '''    for pattern, msg in cobol_checks:
        if re.search(pattern, source, re.IGNORECASE):
            issues.append(msg)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")