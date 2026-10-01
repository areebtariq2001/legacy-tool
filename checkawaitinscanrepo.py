main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("async def scan_repo_endpoint")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

with open("checkawaitinscanrepo_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-'await'-count-inside-function: " + str(body.count("await")) + chr(10))
    out.write("Genuinely-function-body-length: " + str(len(body)))
print("CHECKAWAITINSCANREPO-DONE")