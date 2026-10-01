main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifybatch3_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. logout endpoint exists? ===\n")
    out.write("'/logout' or '/auth/logout' present: " + str("logout" in content.lower()) + chr(10) + chr(10))

    out.write("=== 2. PBKDF2 iterations ===\n")
    idx = content.find("pbkdf2_hmac")
    n = 0
    while idx != -1 and n < 2:
        out.write(content[max(0,idx-20):idx+150] + chr(10) + "---" + chr(10))
        idx = content.find("pbkdf2_hmac", idx+1)
        n += 1
    out.write(chr(10))

    out.write("=== 3. file.read() before size check pattern (safe_read_file) ===\n")
    idx3 = content.find("def safe_read_file")
    idx3_end = content.find("\ndef ", idx3+20)
    out.write(content[idx3:idx3_end][:600])
print("VERIFYBATCH3-DONE")