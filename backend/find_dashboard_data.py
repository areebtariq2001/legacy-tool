with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "def migration_dashboard" in line or "def codebase_history" in line or "migration_dashboard_endpoint" in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("dashboard_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")