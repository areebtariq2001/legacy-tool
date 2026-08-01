import main
import inspect

cobol_src = inspect.getsource(main.migrate_cobol)
lines = cobol_src.split("\n")

output_lines = []
for i, line in enumerate(lines):
    if "compute_m = _mre.match" in line:
        for j in range(max(0, i-1), min(i + 8, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j] + "\n")
        break

with open("compute_context.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")