with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "ALLOWED_ORIGINS" in line or "cors_handler" in line:
        output_lines.append("LINE " + str(i + 1) + ": " + line)
        for j in range(i, min(i + 22, len(lines))):
            if j != i:
                output_lines.append(str(j + 1) + ": " + lines[j])
        break

with open("cors_final_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")