import main
import inspect

src = inspect.getsource(main.migrate_code)
with open("migrate_code_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))