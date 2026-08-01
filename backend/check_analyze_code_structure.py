import main
import inspect

src = inspect.getsource(main.analyze_code)
lines = src.split("\n")

with open("analyze_code_structure.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines[:15]):
        out.write(str(i+1) + ": " + line + "\n")

print("DONE")