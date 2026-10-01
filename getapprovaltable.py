main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("CREATE TABLE IF NOT EXISTS approval_log")
with open("getapprovaltable_result.txt", "w", encoding="utf-8") as out:
    out.write(content[max(0,idx-20):idx+300])
print("GETAPPROVALTABLE-DONE")