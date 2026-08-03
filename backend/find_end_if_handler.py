import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("end_if_handler.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if 'upper.startswith("END-IF")' in line:
            for j in range(i, min(i + 5, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")