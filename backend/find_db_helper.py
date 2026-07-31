with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "_get_db_connection" in line or "def save_approval_decision" in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("db_helper_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")