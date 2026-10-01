main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checksessions_result.txt", "w", encoding="utf-8") as out:
    idx = content.find('@app.post("/auth/register")')
    idx_end = content.find("\n@app.", idx+20)
    out.write(content[idx:idx_end][:800])
print("CHECKSESSIONS-DONE")