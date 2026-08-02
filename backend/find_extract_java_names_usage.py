with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "extract_java_names(" in line and "def " not in line:
        for j in range(max(0,i-2), min(i + 4, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        output_lines.append("---\n")

with open("extract_java_names_usage.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")