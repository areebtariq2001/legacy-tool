with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

endpoints = ["estimate-cost", "detect-tech-stack", "audit-keys", "detect-fraud-gaps", "regional-compliance", "vendor-lockin", "zero-trust-score"]

with open("zzz_7ep_full_out.txt", "w", encoding="utf-8") as out:
    for ep in endpoints:
        idx = content.find('"' + ep + '"')
        chunk = content[idx:idx+800]
        out.write("=== " + ep + " ===\n")
        out.write(chunk + "\n\n")

print("DONE")