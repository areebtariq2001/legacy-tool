with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.post('/extract-business-rules')
async def business_rules_endpoint(file: UploadFile = File(...)):
    try:
        content = await file.read()
        source, error = safe_read_file(content, file.filename)
        if error:
            return JSONResponse(status_code=400, content={'filename': file.filename, 'error': error})
        result = extract_business_rules(source, detect_language(file.filename))
        result['filename'] = file.filename
        return result
    except Exception as e:
        return {'filename': file.filename, 'error': 'Business rule extraction failed safely: ' + str(e)}'''

new = '''@app.post("/extract-business-rules")
async def business_rules_endpoint(file: UploadFile = File(...)):
    try:
        content = await file.read()
        source, error = safe_read_file(content, file.filename)
        if error:
            return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})
        result = extract_business_rules(source, detect_language(file.filename))
        result["filename"] = file.filename
        track_usage("extract-business-rules", file.filename)
        write_audit_log("extract-business-rules", file.filename, "rules extracted via AI")
        return result
    except Exception as e:
        return {"filename": file.filename, "error": f"Business rule extraction failed safely: {e}"}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")