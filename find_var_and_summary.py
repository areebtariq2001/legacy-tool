with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "var -> public" in line or "java_summary" in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("var_and_summary_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")