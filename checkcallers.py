main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkcallers_result.txt", "w", encoding="utf-8") as out:
    out.write("=== save-approval endpoint (caller) ===\n")
    idx1 = content.find('"/save-approval"')
    idx1_end = content.find("\n@app.", idx1+20)
    out.write(content[idx1:idx1_end][:900] + chr(10) + chr(10))

    out.write("=== find_similar_files FULL ===\n")
    idx2 = content.find("def find_similar_files")
    idx2_end = content.find("\ndef ", idx2+20)
    out.write(content[idx2:idx2_end][:1200] + chr(10) + chr(10))

    out.write("=== INSERT into approval_log columns ===\n")
    idx3 = content.find("INSERT INTO approval_log")
    out.write(content[max(0,idx3-30):idx3+200])
print("CHECKCALLERS-DONE")