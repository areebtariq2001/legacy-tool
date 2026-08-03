import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("todo_fallback.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "TODO: manual review" in line:
            for j in range(max(0,i-1), min(i + 3, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")