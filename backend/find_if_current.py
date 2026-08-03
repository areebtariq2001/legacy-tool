import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("if_current.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if 'upper.startswith("IF ")' in line:
            for j in range(i, min(i + 14, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")