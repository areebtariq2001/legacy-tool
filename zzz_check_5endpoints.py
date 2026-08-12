with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

endpoints = ["extract-business-rules", "executive-report", "analyze-impact", "map-transaction-flow", "rollback-plan"]

with open("zzz_5ep_out.txt", "w", encoding="utf-8") as out:
    for ep in endpoints:
        idx = content.find('"' + ep + "'" if False else "'" + ep + "'")
        if idx == -1:
            idx = content.find('"' + ep + '"')
        chunk = content[idx:idx+900]
        has_track = "track_usage" in chunk
        has_audit = "write_audit_log" in chunk
        out.write(ep + " : track_usage=" + str(has_track) + " write_audit_log=" + str(has_audit) + "\n")

print("DONE")