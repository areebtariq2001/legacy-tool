main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("class StarBuildBlockchain")
idx_end = content.find("def add_block", idx)

with open("checkblockchaininit_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("CHECKBLOCKCHAININIT-DONE")