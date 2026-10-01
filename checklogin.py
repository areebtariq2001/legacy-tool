main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def login_user")
idx_end = content.find("\ndef ", idx+20)

with open("checklogin_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("CHECKLOGIN-DONE")