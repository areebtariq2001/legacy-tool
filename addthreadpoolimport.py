main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = "_rate_limit_store = {}\nimport time\nimport urllib.parse"
new = "_rate_limit_store = {}\nimport time\nimport urllib.parse\nfrom starlette.concurrency import run_in_threadpool"

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("ADDTHREADPOOLIMPORT-DONE")
else:
    print("FAILED - count was:", count)