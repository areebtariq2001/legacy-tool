import main
import inspect

cobol_src = inspect.getsource(main.migrate_cobol)
lines = cobol_src.split("\n")

output_lines = []
for i, line in enumerate(lines):
    if "COMPUTE" in line or "compute_m" in line:
        output_lines.append(str(i + 1) + ": " + line + "\n")

with open("compute_section.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")