import main
import inspect

src = inspect.getsource(main.validate_cobol)
with open("validate_cobol_now.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")