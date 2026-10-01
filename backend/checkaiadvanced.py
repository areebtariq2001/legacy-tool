main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkaiadvanced_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("def ai_advanced_migrate")
    idx_end = content.find("\ndef ", idx+20)
    body = content[idx:idx_end]
    out.write("Genuinely-function-length: " + str(len(body)) + chr(10))
    out.write("Genuinely-Low-confidence-fix-count-inside: " + str(body.count("Low confidence - AI failed")) + chr(10))
    out.write("Genuinely-'migrated_code', source-pattern-count: " + str(body.count("'migrated_code', source")) + chr(10) + chr(10))
    idx2 = body.find("elif lang ==")
    n = 0
    while idx2 != -1 and n < 6:
        out.write(body[idx2:idx2+80] + chr(10))
        idx2 = body.find("elif lang ==", idx2+1)
        n += 1
print("CHECKAIADVANCED-DONE")