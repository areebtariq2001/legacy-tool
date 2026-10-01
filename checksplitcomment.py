main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("_split_inline_comment")
idx_end = content.find("\n", idx)

with open("checksplitcomment_result.txt", "w", encoding="utf-8") as out:
    out.write("First-occurrence-context: " + content[max(0,idx-50):idx+400])
print("CHECKSPLITCOMMENT-DONE")