with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("zzz_verify238_out.txt", "w") as out:
    out.write("audit_key_management has REDACTED: " + str("***REDACTED***" in content) + "\n")
    out.write("detect_pii has REDACTED sub logic: " + str("REDACTED" in content) + "\n")
    out.write("score_zero_trust has src_l: " + str("src_l = source.lower()" in content) + "\n")

print("DONE")