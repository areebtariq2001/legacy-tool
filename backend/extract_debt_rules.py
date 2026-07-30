with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "DEBT_RULES" in line and "=" in line:
        output_lines.append(str(i + 1) + ": " + line)
    if "re.findall(pattern" in line or "for pattern, label" in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("debt_rules_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")