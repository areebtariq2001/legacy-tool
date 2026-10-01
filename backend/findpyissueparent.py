main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("py_issue_checks = [")
before = content[:idx]
last_def_idx = before.rfind("\ndef ")

with open("findpyissueparent_result.txt", "w", encoding="utf-8") as out:
    out.write(content[last_def_idx:last_def_idx+60])
print("FINDPYISSUEPARENT-DONE")