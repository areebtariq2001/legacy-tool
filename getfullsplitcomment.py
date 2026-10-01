main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def _split_inline_comment")
idx_end = content.find("\n    for pattern", idx)
if idx_end == -1:
    idx_end = idx + 700

with open("getfullsplitcomment_result.txt", "w", encoding="utf-8") as out:
    out.write(repr(content[idx:idx_end]))
print("GETFULLSPLITCOMMENT-DONE")