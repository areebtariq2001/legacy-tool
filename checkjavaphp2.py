main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkjavaphp2_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-def-migrate_java-count: " + str(content.count("def migrate_java")) + chr(10))
    idx = content.find("def migrate_java(")
    idx_end = content.find("\ndef ", idx+30)
    body = content[idx:idx_end]
    out.write("Genuinely-function-length-chars: " + str(len(body)) + chr(10) + chr(10))
    out.write(body[-500:])
print("CHECKJAVAPHP2-DONE")