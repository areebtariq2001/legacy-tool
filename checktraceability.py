main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('@app.post("/traceability-query"')
idx_end = content.find("\n@app.", idx+20)

with open("checktraceability_result.txt", "w", encoding="utf-8") as out:
    body = content[idx:idx_end]
    idx2 = body.find("call_ai_provider")
    out.write(body[max(0,idx2-100):idx2+200] if idx2 != -1 else "call_ai_provider-NOT-FOUND-checking-other-pattern")
    if idx2 == -1:
        out.write(body[-600:])
print("CHECKTRACEABILITY-DONE")