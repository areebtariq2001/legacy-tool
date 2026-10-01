main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifycert_result.txt", "w", encoding="utf-8") as out:
    out.write("=== issue-migration-certificate endpoint ===\n")
    idx = content.find('@app.post("/issue-migration-certificate")')
    idx_end = content.find("\n@app.", idx+20)
    out.write(content[idx:idx_end] + chr(10) + chr(10))

    out.write("=== MigrationCertificate.issue method ===\n")
    idx2 = content.find("def issue(")
    idx2_end = content.find("\n    def ", idx2+20)
    if idx2_end == -1:
        idx2_end = content.find("\ndef ", idx2+20)
    out.write(content[idx2:idx2_end])
print("VERIFYCERT-DONE")