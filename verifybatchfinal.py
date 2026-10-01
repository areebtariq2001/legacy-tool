main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifybatchfinal_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. deep_verify_python compile usage ===\n")
    idx = content.find("def deep_verify_python")
    idx_end = content.find("\ndef ", idx+20)
    body = content[idx:idx_end]
    out.write("has-compile-call: " + str("compile(" in body) + chr(10))
    out.write("has-exec-of-compiled-result: " + str(bool(__import__("re").search(r"exec\s*\(\s*compile", body))) + chr(10) + chr(10))

    out.write("=== 2. chain trimming direction ===\n")
    idx2 = content.find("del self.chain")
    out.write(content[max(0,idx2-20):idx2+30] + chr(10) + chr(10))

    out.write("=== 6. pan regex ===\n")
    idx3 = content.find(r'\\bpan\\b')
    out.write("double-backslash-found: " + str(idx3 != -1) + chr(10))
    idx3b = content.find(r'\bpan\b')
    out.write("single-backslash-bpan-count: " + str(content.count(r'\bpan\b')) + chr(10) + chr(10))

    out.write("=== 8. assess_dependency_risk call in scan_repo ===\n")
    idx4 = content.find("assess_dependency_risk(source)")
    out.write("assess_dependency_risk(source)-no-filename-count: " + str(content.count("assess_dependency_risk(source)")) + chr(10))
    idx4b = content.find("risk = assess_dependency_risk")
    out.write(content[max(0,idx4b-20):idx4b+60] + chr(10) + chr(10))

    out.write("=== 5. /download endpoint ===\n")
    idx5 = content.find('@app.post("/download"')
    idx5_end = content.find("\n@app.", idx5+20)
    out.write(content[idx5:idx5_end][:500] if idx5 != -1 else "NOT-FOUND")
print("VERIFYBATCHFINAL-DONE")