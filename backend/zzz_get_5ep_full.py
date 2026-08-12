with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

endpoints = ["extract-business-rules", "executive-report", "analyze-impact", "map-transaction-flow", "rollback-plan"]

with open("zzz_5ep_full_out.txt", "w", encoding="utf-8") as out:
    for ep in endpoints:
        idx = content.find("'" + ep + "'")
        if idx == -1:
            idx = content.find('"' + ep + '"')
        chunk = content[idx:idx+900]
        out.write("=== " + ep + " ===\n")
        out.write(chunk + "\n\n")

print("DONE")