main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def _safe_haskey_sub")
# search backward for the enclosing "def " at column 0 (module-level function)
before = content[:idx]
last_def_idx = before.rfind("\ndef ")

with open("findparent_result.txt", "w", encoding="utf-8") as out:
    out.write(content[last_def_idx:last_def_idx+80])
print("FINDPARENT-DONE")