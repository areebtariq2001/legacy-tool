import main
import inspect

cobol_src = inspect.getsource(main.migrate_cobol)
lines = cobol_src.split("\n")

output_lines = []
for i, line in enumerate(lines):
    if "move_m = " in line:
        for j in range(max(0, i-1), min(i + 10, len(lines))):
            output_lines.append(str(j + 1) + ": " + lines[j] + "\n")
        break

with open("move_context.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")