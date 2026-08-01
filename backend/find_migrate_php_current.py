import main
import inspect

php_src = inspect.getsource(main.migrate_php)
lines = php_src.split("\n")

output_lines = []
for i, line in enumerate(lines):
    if "for pattern, repl, label in rules" in line:
        for j in range(i, min(i + 6, len(lines))):
            output_lines.append(str(j) + ": " + lines[j] + "\n")

with open("migrate_php_current.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")