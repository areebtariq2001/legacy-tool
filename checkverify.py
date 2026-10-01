main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("def verify(self, cert_id)")
idx_end = content.find("\n    def ", idx+20)
if idx_end == -1 or idx_end - idx > 2000:
    idx_end = content.find("\n\n\n", idx+20)

with open("checkverify_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("CHECKVERIFY-DONE")