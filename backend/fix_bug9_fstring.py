with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''write_audit_log("tech-debt", file.filename, "score=" + str(result.get("debt_score", 0)) + " hours=" + str(result.get("estimated_hours", 0)))'''
new = '''write_audit_log("tech-debt", file.filename, f"score={result.get('debt_score', 0)} hours={result.get('estimated_hours', 0)}")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")