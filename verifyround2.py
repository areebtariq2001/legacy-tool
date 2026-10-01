main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifyround2_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. hardcoded confidence 90 / High confidence ===\n")
    idx = content.find('"confidence": 90')
    if idx == -1:
        idx = content.find("confidence.*90")
    out.write(content[max(0,idx-300):idx+200] if idx != -1 else "NOT-FOUND-with-exact-string" )
    out.write(chr(10) + chr(10))

    out.write("=== 2. write_audit_log call count ===\n")
    out.write("Total-write_audit_log-calls: " + str(content.count("write_audit_log(")) + chr(10))
print("VERIFYROUND2-DONE")