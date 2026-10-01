main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx1 = content.find("def scan_repo_endpoint")
idx1_end = content.find("\ndef ", idx1+20)
body1 = content[idx1:idx1_end]
idx1b = body1.find('"disclaimer"')

with open("getdisclaimer_result.txt", "w", encoding="utf-8") as out:
    out.write(repr(body1[idx1b:idx1b+300]))
print("GETDISCLAIMER-DONE")