main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifybatch2_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. endpoint_identifier logic ===\n")
    idx1 = content.find("_endpoint_identifier =")
    out.write(content[max(0,idx1-50):idx1+200] + chr(10) + chr(10))

    out.write("=== 2. previous_content ===\n")
    idx2 = content.find("previous_content")
    n = 0
    while idx2 != -1 and n < 3:
        out.write(content[max(0,idx2-100):idx2+100] + chr(10) + "---" + chr(10))
        idx2 = content.find("previous_content", idx2+1)
        n += 1
    out.write(chr(10))

    out.write("=== 3. write_audit_log signature ===\n")
    idx3 = content.find("def write_audit_log")
    idx3_end = content.find("\ndef ", idx3+20)
    out.write(content[idx3:idx3_end][:600] + chr(10) + chr(10))

    out.write("=== 4. StringIO/Queue in check_dependencies rules ===\n")
    idx4 = content.find("StringIO")
    if idx4 != -1:
        out.write(content[max(0,idx4-150):idx4+100])
    else:
        out.write("StringIO-NOT-FOUND")
print("VERIFYBATCH2-DONE")