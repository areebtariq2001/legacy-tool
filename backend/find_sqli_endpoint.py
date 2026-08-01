with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if 'scan-sqli' in line or 'sqli_endpoint' in line:
        output_lines.append("FOUND AT LINE: " + str(i + 1) + "\n")
        for j in range(i, min(i + 10, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        output_lines.append("---\n")

with open("sqli_endpoint_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")