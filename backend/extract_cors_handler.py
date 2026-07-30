with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i in range(14, 45):
    output_lines.append(str(i + 1) + ": " + lines[i])

with open("cors_handler_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")