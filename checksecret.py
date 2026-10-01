main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checksecret_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-'APP_SECRET'-count: " + str(content.count("APP_SECRET")) + chr(10))
    out.write("Genuinely-'SECRET_KEY'-count: " + str(content.count("SECRET_KEY")) + chr(10))
    out.write("Genuinely-'hmac'-count: " + str(content.count("hmac")) + chr(10))
    out.write("Genuinely-'_check_user_auth'-def-exists: " + str("def _check_user_auth" in content) + chr(10))
    idx = content.find("def _check_user_auth")
    idx_end = content.find("\ndef ", idx+20)
    out.write(content[idx:idx_end])
print("CHECKSECRET-DONE")