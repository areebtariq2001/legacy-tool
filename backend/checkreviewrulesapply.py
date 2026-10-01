main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def migrate_java")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

idx2 = body.find("for pattern, msg in review_rules")
if idx2 == -1:
    idx2 = body.find("review_rules:")

with open("checkreviewrulesapply_result.txt", "w", encoding="utf-8") as out:
    out.write(body[idx2-50:idx2+600] if idx2 != -1 else "NOT-FOUND, dumping tail:" + body[-1500:])
print("CHECKREVIEWRULESAPPLY-DONE")