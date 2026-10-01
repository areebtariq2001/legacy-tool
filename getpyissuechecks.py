main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("py_issue_checks = [")
idx_end = content.find("for pattern, msg in py_issue_checks:")

with open("getpyissuechecks_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end+100])
print("GETPYISSUECHECKS-DONE")