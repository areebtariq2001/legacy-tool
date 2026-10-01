main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkblockchain_result.txt", "w", encoding="utf-8") as out:
    out.write("=== AuditBlock class ===\n")
    idx = content.find("class AuditBlock")
    idx_end = content.find("\nclass ", idx+20)
    if idx_end == -1:
        idx_end = idx + 1500
    out.write(content[idx:idx_end] + chr(10) + chr(10))

    out.write("=== StarBuildBlockchain add_block ===\n")
    idx2 = content.find("def add_block")
    idx2_end = content.find("\n    def ", idx2+20)
    out.write(content[idx2:idx2_end] + chr(10) + chr(10))

    out.write("=== verify_chain ===\n")
    idx3 = content.find("def verify_chain")
    idx3_end = content.find("\n    def ", idx3+20)
    out.write(content[idx3:idx3_end])
print("CHECKBLOCKCHAIN-DONE")