import main
import inspect

java_src = inspect.getsource(main.migrate_java)

with open("migrate_java_full.txt", "w", encoding="utf-8") as out:
    out.write(java_src)

print("DONE")