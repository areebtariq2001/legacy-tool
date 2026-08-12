with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

endpoints = ["estimate-cost", "detect-tech-stack", "audit-keys", "detect-fraud-gaps", "regional-compliance", "vendor-lockin", "zero-trust-score"]

with open("zzz_7ep_out.txt", "w", encoding="utf-8") as out:
    for ep in endpoints:
        idx = content.find('"' + ep + '"')
        chunk = content[idx:idx+800]
        has_audit = "write_audit_log" in chunk
        has_jsonresp = "JSONResponse" in chunk
        out.write(ep + " : write_audit_log=" + str(has_audit) + " JSONResponse=" + str(has_jsonresp) + "\n")

print("DONE")