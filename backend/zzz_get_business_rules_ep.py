with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("business_rules_endpoint")
chunk = content[idx-50:idx+600]

with open("zzz_bre_out.txt", "w", encoding="utf-8") as out:
    out.write(chunk)

print("DONE")