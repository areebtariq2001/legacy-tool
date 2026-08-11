with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('"score=" + str(', 'f"score={'),
    ('"risk=" + str(', 'f"risk={'),
    ('"recs=" + str(', 'f"recs={'),
    ('"tables=" + str(', 'f"tables={'),
    ('"libs=" + str(', 'f"libs={'),
    ('"layers=" + str(', 'f"layers={'),
]

with open("zzz_fix_step1_log.txt", "w") as log:
    for old, new in replacements:
        count = content.count(old)
        log.write(f"{count} occurrences of: {old}\n")

print("DONE - checked, not yet patched (need manual close-paren handling)")