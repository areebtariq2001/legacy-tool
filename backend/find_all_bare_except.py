with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if line.strip() == "except:":
        for j in range(i, min(i + 3, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        output_lines.append("---\n")

with open("all_bare_except_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE - found", len(output_lines), "lines")