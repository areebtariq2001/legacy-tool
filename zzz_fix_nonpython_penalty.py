with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        else:
            score -= 10
            findings.append({"issue": "Non-Python file - AI-native structural analysis limited, review manually", "impact": "Low"})'''

new = '''        else:
            findings.append({"issue": "Non-Python file - AI-native structural analysis limited to pattern-based checks below, review manually", "impact": "Low"})'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")