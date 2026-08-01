import main
import inspect

cobol_src = inspect.getsource(main.migrate_cobol)

with open("migrate_cobol_full.txt", "w", encoding="utf-8") as out:
    out.write(cobol_src)

print("DONE - length:", len(cobol_src), "chars")