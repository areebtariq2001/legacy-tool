main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def migrate_php")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

with open("checkmigratephp_result.txt", "w", encoding="utf-8") as out:
    out.write("uses-_split_inline_comment(-count: " + str(body.count("_split_inline_comment(")) + chr(10))
    out.write("has-review_rules-or-similar: " + str("review_rules" in body) + chr(10))
    out.write("has-re.search-on-migrated: " + str("re.search(pattern, migrated)" in body) + chr(10))
print("CHECKMIGRATEPHP-DONE")