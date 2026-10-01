main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("_AUTO_BLOCK_EVENT_TYPES")
with open("checkautoblock_result.txt", "w", encoding="utf-8") as out:
    out.write(content[max(0,idx-10):idx+150])
print("CHECKAUTOBLOCK-DONE")