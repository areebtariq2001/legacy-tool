with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "async def migration_dashboard_endpoint" in line:
        output_lines.append("FOUND AT LINE: " + str(i + 1) + "\n")
        for j in range(i, min(i + 20, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j])
        break

with open("dashboard_output3.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")