main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkroutes3_result.txt", "w", encoding="utf-8") as out:
    for route in ['@app.post("/generate-docs"', '@app.post("/ai-consistency-check"']:
        idx = content.find(route)
        idx_end = content.find("\n@app.", idx+20)
        out.write("=== " + route + " ===\n")
        out.write(content[idx:idx_end][:700] + chr(10) + chr(10))
print("CHECKROUTES3-DONE")