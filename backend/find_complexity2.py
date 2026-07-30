with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if line.strip().startswith("def calculate_complexity("):
        output_lines.append("FOUND AT LINE: " + str(i + 1) + "\n")
        for j in range(i, min(i + 30, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        break

if not output_lines:
    output_lines.append("NOT FOUND - function name may be different\n")

with open("complexity_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")