with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for target in [2113, 2317, 2422, 2697, 2748, 3457]:
    idx = target - 1
    output_lines.append("=== LINE " + str(target) + " ===\n")
    for j in range(idx, min(idx + 20, len(lines))):
        output_lines.append(str(j + 1) + ": " + lines[j])
        if "except" in lines[j] and j > idx:
            for k in range(j, min(j+5, len(lines))):
                output_lines.append(str(k + 1) + ": " + lines[k])
            break
    output_lines.append("\n")

with open("remaining_batch_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")