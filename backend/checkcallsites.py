main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkcallsites_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("_check_endpoint_specific_limit(")
    count = 0
    while idx != -1 and count < 10:
        line_start = content.rfind(chr(10), 0, idx) + 1
        line_end = content.find(chr(10), idx)
        out.write(content[line_start:line_end].strip() + chr(10))
        idx = content.find("_check_endpoint_specific_limit(", idx+1)
        count += 1
print("CHECKCALLSITES-DONE")