main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifyfinal_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. fake confidence search ===\n")
    for phrase in ['"confidence": 90', "'confidence': 90", '"High confidence"', "confidence_score.*90", "valid.*True.*verified.*True"]:
        out.write(phrase + " -> count: " + str(content.count(phrase)) + chr(10))
    idx = content.find("_create_users_table_if_needed")
    out.write(chr(10) + "=== 2. per-request DDL (_create_users_table_if_needed calls) ===\n")
    out.write("Total-calls: " + str(content.count("_create_users_table_if_needed(cur)")) + chr(10))
    idx2_end = content.find("\ndef ", idx+20)
    out.write(content[idx:idx2_end][:400] + chr(10) + chr(10))

    out.write("=== 3. file.read() before safe_read_file pattern ===\n")
    idx3 = content.find("await file.read()")
    n = 0
    while idx3 != -1 and n < 2:
        out.write(content[idx3:idx3+250] + chr(10) + "---" + chr(10))
        idx3 = content.find("await file.read()", idx3+1)
        n += 1
print("VERIFYFINAL-DONE")