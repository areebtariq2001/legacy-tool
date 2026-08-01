with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
target = 568
for i in range(max(0, target - 15), target + 2):
    output_lines.append(str(i + 1) + ": " + lines[i])

with open("parse_context_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")