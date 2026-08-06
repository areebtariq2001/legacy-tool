import main
with open("sensitive_patterns_output.txt", "w", encoding="utf-8") as out:
    for p, label, sev in main.SENSITIVE_PATTERNS:
        out.write(repr(p) + " | " + label + " | " + sev + "\n")

print("DONE")