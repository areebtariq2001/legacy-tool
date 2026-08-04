with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if '"/download"' in line or "'/download'" in line:
        for j in range(i, min(i + 30, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        break

with open("download_endpoint_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")