with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for target in [1714, 1873, 1891]:
    idx = target - 1
    output_lines.append("=== AROUND LINE " + str(target) + " ===\n")
    for j in range(max(0, idx - 5), min(idx + 5, len(lines))):
        output_lines.append(str(j + 1) + ": " + lines[j])
    output_lines.append("\n")

with open("remaining_excepts_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")