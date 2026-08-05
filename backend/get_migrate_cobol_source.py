import main
import inspect

src = inspect.getsource(main.migrate_cobol_endpoint)
with open("migrate_cobol_source.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")