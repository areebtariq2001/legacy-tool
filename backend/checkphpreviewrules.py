main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def migrate_php")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

idx2 = body.find("re.search(pattern, migrated)")

with open("checkphpreviewrules_result.txt", "w", encoding="utf-8") as out:
    out.write(body[max(0,idx2-300):idx2+150])
print("CHECKPHPREVIEWRULES-DONE")