main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("diag3_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("CBS")
    n = 0
    while idx != -1 and n < 5:
        out.write("--- Occurrence " + str(n+1) + " ---\n")
        out.write(repr(content[max(0,idx-10):idx+80]) + chr(10) + chr(10))
        idx = content.find("CBS", idx+1)
        n += 1
print("DIAG3-DONE")