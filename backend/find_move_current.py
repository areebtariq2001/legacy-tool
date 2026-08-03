import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("move_current.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "move_m = re.match" in line:
            for j in range(i, min(i + 10, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")