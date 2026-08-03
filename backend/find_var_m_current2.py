import main
import inspect

src = inspect.getsource(main.migrate_cobol)
lines = src.split("\n")

with open("var_m_current2.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "var_m = re.match" in line:
            for j in range(i, min(i + 14, len(lines))):
                out.write(str(j) + ": " + lines[j] + "\n")
            break

print("DONE")