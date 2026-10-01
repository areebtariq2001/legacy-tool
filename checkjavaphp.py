main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkjavaphp_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("def migrate_java")
    idx_end = content.find("\ndef ", idx+20)
    body = content[idx:idx_end]
    out.write("=== migrate_java disclaimer/return ===\n")
    ridx = body.rfind("return")
    out.write(body[max(0,ridx-100):ridx+400])
print("CHECKJAVAPHP-DONE")