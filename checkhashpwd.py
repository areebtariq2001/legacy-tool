main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def _hash_password")
idx_end = content.find("\ndef ", idx+20)

with open("checkhashpwd_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("CHECKHASHPWD-DONE")