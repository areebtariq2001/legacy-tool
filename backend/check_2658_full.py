with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i in range(2654, 2680):
    output_lines.append(str(i + 1) + ": " + lines[i])

with open("check_2658_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")