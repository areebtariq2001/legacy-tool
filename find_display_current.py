import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("display_current.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "disp_m = re.match" in line:
            for j in range(i, min(i + 8, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")