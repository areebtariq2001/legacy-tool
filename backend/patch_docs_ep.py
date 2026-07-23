with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_idx = None
for i, line in enumerate(lines):
    if line.strip() == "@app.get('/')":
        target_idx = i
        break

if target_idx is None:
    print("TARGET NOT FOUND - ABORT")
else:
    endpoint_code = '''@app.post("/living-docs")
async def living_docs_endpoint(file: UploadFile = File(...)):
    try:
        content = await file.read()
        source, error = safe_read_file(content, file.filename)
        if error:
            return {"filename": file.filename, "error": error}
        result = generate_living_documentation(source, file.filename)
        result["filename"] = file.filename
        track_usage("living-docs", file.filename)
        return result
    except Exception as e:
        return {"filename": file.filename, "error": "Living documentation generation failed safely: " + str(e)}

'''
    lines.insert(target_idx, endpoint_code)
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY at line", target_idx)