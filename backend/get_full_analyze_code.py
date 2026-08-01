import main
import inspect

src = inspect.getsource(main.analyze_code)

with open("full_analyze_code.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))