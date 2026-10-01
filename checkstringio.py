main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkstringio_result.txt", "w", encoding="utf-8") as out:
    out.write("=== def get_why_explanations or def check_dependencies logic ===\n")
    idx = content.find("def check_dependencies")
    if idx == -1:
        idx = content.find("def get_why_explanations")
    idx_end = content.find("\ndef ", idx+20)
    out.write(content[idx:idx_end][:1500])
print("CHECKSTRINGIO-DONE")