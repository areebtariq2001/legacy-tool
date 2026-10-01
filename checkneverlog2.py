main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("_NEVER_LOG_PATTERNS")

with open("checkneverlog2_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx+700])
print("CHECKNEVERLOG2-DONE")