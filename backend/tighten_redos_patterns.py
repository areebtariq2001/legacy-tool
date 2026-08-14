import re as pyre

with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

original_count_pwd = len(pyre.findall(r"\[\\w-\]\*\(password\|passwd\|pwd\)\[\\w-\]\*\\s\+PIC\\s\+X\.\*VALUE", content))
original_count_user = len(pyre.findall(r"\[\\w-\]\*\(username\|user_name\|db\.\?user\)\[\\w-\]\*\\s\+PIC\\s\+X\.\*VALUE", content))

content = content.replace(
    r"[\w-]*(password|passwd|pwd)[\w-]*\s+PIC\s+X.*VALUE\s+",
    r"\b(password|passwd|pwd)[\w-]*\s+PIC\s+X[^\n]{0,80}?VALUE\s+"
)
content = content.replace(
    r"[\w-]*(username|user_name|db.?user)[\w-]*\s+PIC\s+X.*VALUE\s+",
    r"\b(username|user_name|db.?user)[\w-]*\s+PIC\s+X[^\n]{0,80}?VALUE\s+"
)
content = content.replace(
    r"[\w-]*password[\w-]*\s+PIC\s+X.*VALUE\s+",
    r"\bpassword[\w-]*\s+PIC\s+X[^\n]{0,80}?VALUE\s+"
)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

with open("tighten_log.txt", "w") as log:
    log.write("original_count_pwd_pattern: " + str(original_count_pwd) + "\n")
    log.write("original_count_user_pattern: " + str(original_count_user) + "\n")

print("TIGHTEN-COMPLETED")