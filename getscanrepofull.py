main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("async def scan_repo_endpoint")
idx_end = content.find("\n@app.", idx+20)
if idx_end == -1 or idx_end - idx > 6000:
    idx_end = content.find("\ndef ", idx+3000)

with open("getscanrepofull_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end][:400] + chr(10) + "...[TRUNCATED-MIDDLE]..." + chr(10) + content[idx_end-400:idx_end])
    out.write(chr(10) + chr(10) + "Genuinely-total-length: " + str(idx_end - idx))
print("GETSCANREPOFULL-DONE")