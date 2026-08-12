with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = 'async def regional_compliance_endpoint(file: UploadFile = File(...), region: str = "Pakistan"):\n    try:\n        content = await file.read()'
new = 'async def regional_compliance_endpoint(file: UploadFile = File(...), region: str = "Pakistan"):\n    try:\n        _allowed_regions = {"Pakistan", "Global"}\n        if region not in _allowed_regions:\n            return JSONResponse(status_code=400, content={"filename": file.filename, "error": "Invalid region. Allowed: " + ", ".join(_allowed_regions)})\n        content = await file.read()'
count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")