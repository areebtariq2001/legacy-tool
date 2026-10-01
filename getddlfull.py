main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def _create_users_table_if_needed")
idx_end = content.find("\ndef ", idx+20)

with open("getddlfull_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("GETDDLFULL-DONE")