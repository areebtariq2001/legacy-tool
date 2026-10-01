main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifyfinalbatch2_result.txt", "w", encoding="utf-8") as out:
    out.write("=== Bug 1: compile() exec-of-result check ===\n")
    idx = content.find("def deep_verify_python")
    idx_end = content.find("\ndef ", idx+20)
    body = content[idx:idx_end]
    out.write("has-compile-call: " + str("compile(" in body) + chr(10))
    out.write("has-exec-of-compiled-result: " + str(bool(__import__("re").search(r"exec\s*\(\s*compile", body))) + chr(10) + chr(10))

    out.write("=== Bug 2: Groq model name ===\n")
    idx2 = content.find('"model":')
    out.write(content[idx2:idx2+80] + chr(10) + chr(10))

    out.write("=== Bug 3: blockchain del direction + head_hash presence ===\n")
    idx3 = content.find("del self.chain")
    out.write(content[max(0,idx3-20):idx3+30] + chr(10))
    out.write("has-_head_hash: " + str("_head_hash" in content) + chr(10))
    out.write("has-proof-of-work-check-in-verify_chain: " + str("_difficulty_prefix" in content) + chr(10) + chr(10))

    out.write("=== Bug 4: track_usage function ===\n")
    idx4 = content.find("def track_usage")
    idx4_end = content.find("\ndef ", idx4+20)
    out.write(content[idx4:idx4_end] + chr(10) + chr(10))

    out.write("=== Bug 5: /download endpoint try/except ===\n")
    idx5 = content.find('@app.post("/download"')
    idx5_end = content.find("\n@app.", idx5+20)
    out.write(content[idx5:idx5_end][:800])
print("VERIFYFINALBATCH2-DONE")