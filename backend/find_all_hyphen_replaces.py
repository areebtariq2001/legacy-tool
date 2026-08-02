import main
import inspect

src = inspect.getsource(main.migrate_cobol)
count = src.count('.replace("-", "_")')
with open("hyphen_replace_count.txt", "w", encoding="utf-8") as out:
    out.write("Count of .replace(-,_): " + str(count) + "\n")

print("DONE")