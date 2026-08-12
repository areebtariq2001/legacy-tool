with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = 'findings.append({"line": i+1, "type": label, "code": _redacted})'
new = 'findings.append({"line": i+1, "type": label, "code": _redacted, "evidence": "Line " + str(i+1) + " (" + label + "): " + _redacted})'
count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")