with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if ('open("' in line or "open('" in line) and ('.json' in line or '.txt' in line or '.csv' in line or '.log' in line):
        output_lines.append(str(i + 1) + ": " + line)

with open("other_files_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")