main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("diag4_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("legacy CBS integration")
    out.write(repr(content[max(0,idx-150):idx+400]))
print("DIAG4-DONE")