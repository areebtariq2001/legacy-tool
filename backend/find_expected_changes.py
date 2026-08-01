with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "expected_changes" in line and "=" in line and "{" in line:
        output_lines.append("FOUND AT LINE: " + str(i + 1) + "\n")
        for j in range(max(0,i-2), min(i + 8, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        break

with open("expected_changes_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")