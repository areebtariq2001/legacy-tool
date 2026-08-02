import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("perform_until_current.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "perform_m = re.match" in line:
            for j in range(i, min(i + 20, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")