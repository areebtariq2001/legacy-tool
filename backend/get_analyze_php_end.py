import main
import inspect

src = inspect.getsource(main.analyze_php)
with open("analyze_php_end.txt", "w", encoding="utf-8") as out:
    out.write(src[-800:])

print("DONE")