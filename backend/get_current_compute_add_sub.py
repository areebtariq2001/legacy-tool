import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("current_compute_add_sub.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "COMPUTE" in line or "ADD" in line or "SUBTRACT" in line:
            for j in range(i, min(i + 4, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            out.write("---\n")

print("DONE")