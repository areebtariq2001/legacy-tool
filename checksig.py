main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checksig_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("def save_approval_decision")
    out.write(content[idx:idx+120])
print("CHECKSIG-DONE")