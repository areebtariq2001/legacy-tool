main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkusagelog_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-'CREATE TABLE IF NOT EXISTS usage_log'-count: " + str(content.count("CREATE TABLE IF NOT EXISTS usage_log")) + chr(10))
    out.write("Genuinely-'INSERT INTO usage_log'-count: " + str(content.count("INSERT INTO usage_log")) + chr(10) + chr(10))
    idx = content.find("def write_audit_log")
    idx_end = content.find("\ndef ", idx+20)
    out.write(content[idx:idx_end])
print("CHECKUSAGELOG-DONE")