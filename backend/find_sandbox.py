with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "def run_sandboxed_migration_test" in line or "def _run_single_sandbox" in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("sandbox_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")