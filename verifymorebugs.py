main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifymorebugs_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 9. split/join count inside migrate_code ===\n")
    idx = content.find("def migrate_code")
    idx_end = content.find("\ndef ", idx+20)
    body = content[idx:idx_end]
    out.write("split-count: " + str(body.count("split(chr(10))")) + chr(10))
    out.write("join-count: " + str(body.count("chr(10).join")) + chr(10) + chr(10))

    out.write("=== 13. import time placement ===\n")
    idx2 = content.find("import time")
    out.write(content[max(0,idx2-80):idx2+30] + chr(10) + chr(10))

    out.write("=== 15. import time as _time_mod ===\n")
    idx3 = content.find("import time as _time_mod")
    out.write("found-count: " + str(content.count("import time as _time_mod")) + chr(10))
    out.write(content[max(0,idx3-100):idx3+50] if idx3 != -1 else "NOT-FOUND")
print("VERIFYMOREBUGS-DONE")