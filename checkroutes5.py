main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkroutes5_result.txt", "w", encoding="utf-8") as out:
    for route in ['@app.post("/auth/login"', '@app.post("/auth/register"', '@app.post("/save-approval"']:
        idx = content.find(route)
        idx_end = content.find("\n\n", idx+20)
        out.write("=== " + route + " ===\n")
        out.write(content[idx:idx_end][:400] + chr(10) + chr(10))
print("CHECKROUTES5-DONE")