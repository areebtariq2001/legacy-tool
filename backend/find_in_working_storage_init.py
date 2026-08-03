import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("in_ws_init.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "in_working_storage = False" in line:
            for j in range(max(0,i-2), min(i + 4, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")