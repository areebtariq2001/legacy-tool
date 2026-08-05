with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.post("/migrate-cobol")
async def migrate_cobol_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
    result = migrate_cobol(source)
    result["filename"] = file.filename
    track_usage("migrate-cobol", file.filename)
    write_audit_log("migrate-cobol", file.filename, f"changes={len(result.get('changes', []))}")
    return result'''

new = '''@app.post("/migrate-cobol")
async def migrate_cobol_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
    try:
        pre_analysis = analyze_cobol(source)
        pre_issues = pre_analysis.get("issues", [])
    except Exception:
        pre_issues = []
    result = migrate_cobol(source)
    result["filename"] = file.filename
    result["pre_migration_issues"] = pre_issues
    track_usage("migrate-cobol", file.filename)
    write_audit_log("migrate-cobol", file.filename, f"changes={len(result.get('changes', []))}")
    return result'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")