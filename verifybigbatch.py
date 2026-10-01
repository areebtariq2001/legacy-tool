main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifybigbatch_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. save-approval / approval_log ===\n")
    idx1 = content.find("def save_approval")
    if idx1 == -1:
        idx1 = content.find('"/save-approval"')
    idx1_end = content.find("\ndef ", idx1+20)
    out.write(content[idx1:idx1_end][:800] + chr(10) + chr(10))

    out.write("=== 2. similar_files ===\n")
    idx2 = content.find("similar_files")
    n = 0
    while idx2 != -1 and n < 2:
        out.write(content[max(0,idx2-150):idx2+100] + chr(10) + "---" + chr(10))
        idx2 = content.find("similar_files", idx2+1)
        n += 1
    out.write(chr(10))

    out.write("=== 3. str(e) count ===\n")
    out.write("str(e)-occurrences: " + str(content.count("str(e)")) + chr(10) + chr(10))

    out.write("=== 4. compilation passed / execution-ready claim ===\n")
    idx4 = content.find("execution-ready")
    out.write(content[max(0,idx4-200):idx4+100] if idx4 != -1 else "NOT-FOUND")
print("VERIFYBIGBATCH-DONE")