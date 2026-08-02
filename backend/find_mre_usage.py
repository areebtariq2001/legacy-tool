import main
import inspect

src = inspect.getsource(main.migrate_cobol)
count = src.count("_mre")
with open("mre_usage_output.txt", "w", encoding="utf-8") as out:
    out.write("_mre usage count: " + str(count) + "\n")

print("DONE")