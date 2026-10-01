main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def _scan_repo_blocking")
idx_end = content.find("\ndef ", idx+20)
body = content[idx:idx_end]

with open("checktimemod_result.txt", "w", encoding="utf-8") as out:
    out.write("_time_mod-usage-count: " + str(body.count("_time_mod")) + chr(10))
    out.write("local-var-named-'time'-count: " + str(len(__import__("re").findall(r"^\s*time\s*=", body, __import__("re").MULTILINE))) + chr(10))
    idx2 = body.find("_time_mod")
    while idx2 != -1:
        out.write(body[max(0,idx2-20):idx2+30].replace(chr(10), " | ") + chr(10))
        idx2 = body.find("_time_mod", idx2+1)
print("CHECKTIMEMOD-DONE")