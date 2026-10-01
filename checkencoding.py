main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkencoding_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("def safe_read_file")
    idx_end = content.find("\ndef ", idx+20)
    out.write(content[idx:idx_end])
print("CHECKENCODING-DONE")