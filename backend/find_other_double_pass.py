with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "for pattern" in line and "in" in line:
        for j in range(i, min(i + 5, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        output_lines.append("---\n")

with open("other_double_pass_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE - found", len(output_lines), "lines")