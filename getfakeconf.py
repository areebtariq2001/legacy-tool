main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("getfakeconf_result.txt", "w", encoding="utf-8") as out:
    idx1 = content.find('"confidence_score": 90')
    out.write("=== Occurrence-1 (score-90) ===\n")
    out.write(content[max(0,idx1-100):idx1+300] + chr(10) + chr(10))

    idx2 = content.find('"confidence_score"] = 95')
    out.write("=== Occurrence-2 (score-95, first) ===\n")
    out.write(content[max(0,idx2-200):idx2+400] + chr(10) + chr(10))

    idx3 = content.find('"confidence_score"] = 95', idx2+1)
    out.write("=== Occurrence-3 (score-95, second) ===\n")
    out.write(content[max(0,idx3-200):idx3+400])
print("GETFAKECONF-DONE")