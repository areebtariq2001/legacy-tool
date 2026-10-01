main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkjavalang_result.txt", "w", encoding="utf-8") as out:
    out.write("javalang-import-count: " + str(content.count("import javalang")) + chr(10))
    out.write("javalang-usage-count: " + str(content.count("javalang.")) + chr(10) + chr(10))
    idx = content.find("import javalang")
    out.write(content[max(0,idx-50):idx+50] + chr(10) + chr(10))
    idx2 = 0
    count = 0
    while count < 5:
        idx2 = content.find("javalang.", idx2)
        if idx2 == -1:
            break
        line_start = content.rfind(chr(10), 0, idx2) + 1
        line_end = content.find(chr(10), idx2)
        out.write(content[line_start:line_end].strip() + chr(10))
        idx2 += 1
        count += 1
print("CHECKJAVALANG-DONE")