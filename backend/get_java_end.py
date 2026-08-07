import main
import inspect

src = inspect.getsource(main.analyze_java)
with open("java_end.txt", "w", encoding="utf-8") as out:
    out.write(src[-900:])

print("DONE")