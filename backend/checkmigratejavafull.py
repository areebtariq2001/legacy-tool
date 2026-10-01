main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def migrate_java")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

with open("checkmigratejavafull_result.txt", "w", encoding="utf-8") as out:
    out.write(body[:3500])
print("CHECKMIGRATEJAVAFULL-DONE")