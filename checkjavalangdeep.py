main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkjavalangdeep_result.txt", "w", encoding="utf-8") as out:
    idx = 0
    count = 0
    while count < 2:
        idx = content.find("javalang.parse.parse", idx)
        if idx == -1:
            break
        line_start = content.rfind(chr(10), 0, idx)
        func_start = content.rfind("\ndef ", 0, idx)
        out.write("=== Usage " + str(count+1) + " (function context) ===" + chr(10))
        out.write(content[func_start:idx+400] + chr(10) + chr(10))
        idx += 1
        count += 1
print("CHECKJAVALANGDEEP-DONE")