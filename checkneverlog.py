main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("_NEVER_LOG_PATTERNS")
idx_end = content.find("]", idx) + 1

with open("checkneverlog_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("CHECKNEVERLOG-DONE")