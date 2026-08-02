with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for target in [275, 491, 2113, 2317, 2422, 2658, 2697, 2748, 3457]:
    idx = target - 1
    output_lines.append("=== LINE " + str(target) + " ===\n")
    for j in range(max(0, idx - 3), min(idx + 5, len(lines))):
        output_lines.append(str(j + 1) + ": " + lines[j])
    output_lines.append("\n")

with open("remaining_ast_calls_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")