main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("verify4lines_result.txt", "w", encoding="utf-8") as out:
    for lineno in [8443, 8474, 9006, 9340]:
        out.write("=== Line " + str(lineno) + " area ===\n")
        for i in range(max(0, lineno-3), min(len(lines), lineno+4)):
            out.write(str(i+1) + ": " + lines[i])
        out.write(chr(10))
print("VERIFY4LINES-DONE")