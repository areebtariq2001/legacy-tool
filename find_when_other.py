import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("when_other_current.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if 'upper.startswith("WHEN OTHER")' in line:
            for j in range(i, min(i + 9, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")