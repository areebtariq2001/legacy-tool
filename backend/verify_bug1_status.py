import main
import inspect

src = inspect.getsource(main.migrate_cobol)
with open("bug1_status_output.txt", "w", encoding="utf-8") as out:
    out.write("_mre still present: " + str("_mre" in src) + "\n")
    out.write("_seqre still present: " + str("_seqre" in src) + "\n")

print("DONE")