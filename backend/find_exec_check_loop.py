with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "'exec '" in line:
        for j in range(max(0, i-5), min(i + 10, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        break

with open("exec_check_loop_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")