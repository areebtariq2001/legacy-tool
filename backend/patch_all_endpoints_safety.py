with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

patches = [
    ('''async def analyze_php_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = analyze_php(source)''',
     '''async def analyze_php_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return {"filename": file.filename, "error": error}
    result = analyze_php(source)'''),

    ('''async def migrate_php_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = migrate_php(source)''',
     '''async def migrate_php_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return {"filename": file.filename, "error": error}
    result = migrate_php(source)'''),

    ('''async def analyze_java_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = analyze_java(source)''',
     '''async def analyze_java_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return {"filename": file.filename, "error": error}
    result = analyze_java(source)'''),

    ('''async def migrate_java_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = migrate_java(source)''',
     '''async def migrate_java_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return {"filename": file.filename, "error": error}
    result = migrate_java(source)'''),

    ('''async def analyze_cobol_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = analyze_cobol(source)''',
     '''async def analyze_cobol_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return {"filename": file.filename, "error": error}
    result = analyze_cobol(source)'''),

    ('''async def migrate_cobol_endpoint(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = migrate_cobol(source)''',
     '''async def migrate_cobol_endpoint(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return {"filename": file.filename, "error": error}
    result = migrate_cobol(source)'''),
]

total_patched = 0
for old, new in patches:
    count = content.count(old)
    if count == 1:
        content = content.replace(old, new, 1)
        total_patched += 1
    else:
        print("MISMATCH for a pattern - found", count, "occurrences, expected 1")

print("Total patched:", total_patched, "out of 6")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")