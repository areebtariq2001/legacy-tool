import main
with open("banking_patterns_output.txt", "w", encoding="utf-8") as out:
    for p, label, note in main.BANKING_PATTERNS:
        out.write(repr(p) + " | " + label + "\n")

print("DONE")