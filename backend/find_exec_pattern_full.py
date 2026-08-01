with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "'exec '" in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("exec_pattern_full_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")