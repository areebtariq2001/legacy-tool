with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i in range(2123, 2145):
    output_lines.append(str(i + 1) + ": " + lines[i])

with open("check_2113_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")