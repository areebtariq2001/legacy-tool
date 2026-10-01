main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def migrate_java")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

with open("checkmigratejava_result.txt", "w", encoding="utf-8") as out:
    out.write("migrate_java-body-length: " + str(len(body)) + chr(10))
    out.write("uses-javalang: " + str("javalang" in body) + chr(10))
    out.write("uses-re.sub-or-re.finditer: " + str("re.sub(" in body or "re.finditer(" in body) + chr(10))
    out.write("re.sub-count: " + str(body.count("re.sub(")) + chr(10))
print("CHECKMIGRATEJAVA-DONE")