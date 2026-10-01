main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old3 = '    if not re.match(r"^[\\w.-]+$", owner) or not re.match(r"^[\\w.-]+$", repo):\n        return {"error": "Invalid owner or repo name in the URL - only letters, numbers, dots, hyphens, and underscores are allowed."}'
new3 = '    if not re.match(r"^[\\w.-]+$", owner) or not re.match(r"^[\\w.-]+$", repo) or ".." in owner or ".." in repo:\n        return {"error": "Invalid owner or repo name in the URL - only letters, numbers, dots, hyphens, and underscores are allowed."}'

remaining_count = content.count(old3)
print("Remaining unfixed occurrences:", remaining_count)
if remaining_count >= 1:
    content = content.replace(old3, new3, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXSECOND-DONE")
else:
    print("NO-MORE-TO-FIX")