with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "except Exception:" in line and i+1 < len(lines) and "pass" in lines[i+1]:
        for j in range(max(0,i-5), min(i + 2, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        output_lines.append("---\n")

with open("silent_pass_locations.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")