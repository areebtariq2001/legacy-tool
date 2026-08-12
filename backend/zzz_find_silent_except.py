import re

with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("zzz_silent_except_out.txt", "w", encoding="utf-8") as out:
    count = 0
    for i, line in enumerate(lines):
        if re.match(r"^\s*except.*:\s*$", line):
            if i+1 < len(lines) and re.match(r"^\s*pass\s*$", lines[i+1]):
                out.write(str(i+1) + ": " + line.rstrip() + " -> pass\n")
                count += 1
    out.write("\nTotal genuinely found: " + str(count))

print("DONE")