main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkhmac_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("hmac")
    n = 0
    while idx != -1 and n < 9:
        out.write("--- " + str(n+1) + " ---\n")
        out.write(content[max(0,idx-60):idx+60] + chr(10) + chr(10))
        idx = content.find("hmac", idx+1)
        n += 1
print("CHECKHMAC-DONE")