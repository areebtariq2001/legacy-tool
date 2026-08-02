import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("identification_div_output.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "IDENTIFICATION DIVISION" in line:
            for j in range(i, min(i + 4, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")

print("DONE")