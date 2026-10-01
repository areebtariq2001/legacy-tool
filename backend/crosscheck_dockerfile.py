main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('@app.post("/ai-migrate")')
idx_end = content.find('\n@app.', idx+30)

with open("crosscheck_dockerfile_result.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("CROSSCHECK-DOCKERFILE-DONE")