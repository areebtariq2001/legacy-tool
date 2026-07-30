with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "CORSMiddleware" in line or "cors_handler" in line or "add_middleware" in line or "Access-Control" in line:
        output_lines.append(str(i + 1) + ": " + lines[i])

with open("cors_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")