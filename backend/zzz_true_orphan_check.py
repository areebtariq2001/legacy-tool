import main
import re as pyre

with open("main.py", "r", encoding="utf-8") as f:
    main_source = f.read()

with open("zzz_orphan_final.txt", "w", encoding="utf-8") as out:
    for r in main.app.routes:
        if hasattr(r, 'path') and hasattr(r, 'methods') and 'POST' in (r.methods or []):
            path = r.path
            path_no_slash = path.lstrip("/")
            count = main_source.count("'" + path + "'") + main_source.count('"' + path + '"')
            out.write(path + " : " + str(count) + " occurrence(s) in main.py\n")

print("DONE")