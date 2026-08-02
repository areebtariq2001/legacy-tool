import main
import inspect

src = inspect.getsource(main.migrate_cobol)

with open("final_seqre_mre_check.txt", "w", encoding="utf-8") as out:
    out.write("import re as _seqre present: " + str("import re as _seqre" in src) + "\n")
    out.write("import re as _mre present: " + str("import re as _mre" in src) + "\n")
    out.write("_seqre. usage count: " + str(src.count("_seqre.")) + "\n")
    out.write("_mre. usage count: " + str(src.count("_mre.")) + "\n")

print("DONE")