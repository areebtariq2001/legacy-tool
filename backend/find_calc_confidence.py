with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "def calculate_confidence" in line:
        output_lines.append("DEF FOUND AT LINE: " + str(i + 1) + "\n")
        output_lines.append(str(i + 1) + ": " + lines[i])
    if "calculate_confidence(" in line and "def " not in line:
        output_lines.append("CALL AT LINE " + str(i + 1) + ": " + lines[i])

with open("calc_confidence_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")