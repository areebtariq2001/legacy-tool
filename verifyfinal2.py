main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifyfinal2_result.txt", "w", encoding="utf-8") as out:
    out.write("=== High confidence contexts ===\n")
    idx = content.find('"High confidence"')
    n = 0
    while idx != -1 and n < 5:
        out.write(content[max(0,idx-200):idx+50] + chr(10) + "---" + chr(10))
        idx = content.find('"High confidence"', idx+1)
        n += 1

    out.write(chr(10) + "=== file.read() total count ===\n")
    out.write("Total: " + str(content.count("await file.read()")))
print("VERIFYFINAL2-DONE")