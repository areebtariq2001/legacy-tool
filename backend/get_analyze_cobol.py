import main
import inspect

src = inspect.getsource(main.analyze_cobol)

with open("analyze_cobol_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))