import main
import inspect

src = inspect.getsource(main.migrate_cobol)
count = src.count("_seqre")
with open("seqre_usage_output.txt", "w", encoding="utf-8") as out:
    out.write("_seqre usage count: " + str(count) + "\n")

print("DONE")