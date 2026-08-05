with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''@app.post("/ai-suggest")
async def ai_suggest_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = ai_suggest(source, detect_language(file.filename))
    result["filename"] = file.filename
    track_usage("ai-suggest", file.filename)
    return result

@app.post("/explain")
async def explain_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = ai_explain(source, detect_language(file.filename))
    result["filename"] = file.filename
    track_usage("explain", file.filename)
    return result

@app.post("/generate-tests")
async def generate_tests_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = ai_generate_tests(source, detect_language(file.filename))
    result["filename"] = file.filename
    track_usage("generate-tests", file.filename)
    return result

@app.get("/stats")
def get_stats():
    return load_stats()

@app.get("/audit-log")
def get_audit_log():
    with _stats_lock:
        recent = list(_in_memory_audit_log[:50])
    return {"total_entries": len(recent), "recent": recent}'''

new1 = '''@app.post("/ai-suggest")
async def ai_suggest_endpoint(file: UploadFile = File(...)):
    content = await file.read()
    source, error = safe_read_file(content, file.filename)
    if error:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
    result = ai_suggest(source, detect_language(file.filename))
    result["filename"] = file.filename
    track_usage("ai-suggest", file.filename)
    write_audit_log("ai-suggest", file.filename, "ok")
    return result

@app.post("/explain")
async def explain_endpoint(file: UploadFile = File(...)):
    content = await file.read()
    source, error = safe_read_file(content, file.filename)
    if error:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
    result = ai_explain(source, detect_language(file.filename))
    result["filename"] = file.filename
    track_usage("explain", file.filename)
    write_audit_log("explain", file.filename, "ok")
    return result

@app.post("/generate-tests")
async def generate_tests_endpoint(file: UploadFile = File(...)):
    content = await file.read()
    source, error = safe_read_file(content, file.filename)
    if error:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
    result = ai_generate_tests(source, detect_language(file.filename))
    result["filename"] = file.filename
    track_usage("generate-tests", file.filename)
    write_audit_log("generate-tests", file.filename, "ok")
    return result

@app.get("/stats")
def get_stats():
    return load_stats()

@app.get("/audit-log")
def get_audit_log():
    with _stats_lock:
        all_entries = list(_in_memory_audit_log)
        recent = all_entries[:50]
    return {"total_entries": len(all_entries), "recent": recent}'''

count1 = content.count(old1)
print("Occurrences found:", count1)
if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")