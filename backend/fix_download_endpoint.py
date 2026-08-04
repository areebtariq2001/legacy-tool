with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.post("/download")
async def download(file: UploadFile = File(...)):
    source = (await file.read()).decode("utf-8", errors='ignore')
    result = migrate_code(source)
    migrated = result.get("migrated_code", "")
    filename = file.filename
    if filename.endswith('.py'):
        filename = filename.replace('.py', '_migrated.py')
    return Response(
        content=migrated.encode('utf-8'),
        media_type='application/octet-stream',
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )'''

new = '''@app.post("/download")
async def download(file: UploadFile = File(...)):
    content_bytes = await file.read()
    source, error = safe_read_file(content_bytes, file.filename)
    if error:
        return Response(content=error.encode('utf-8'), media_type='text/plain', status_code=400)
    lang = detect_language(file.filename)
    if lang == "java":
        result = migrate_java(source)
    elif lang == "php":
        result = migrate_php(source)
    elif lang == "cobol":
        result = migrate_cobol(source)
    else:
        result = migrate_code(source)
    migrated = result.get("migrated_code", "")
    filename = file.filename
    ext_map = {'.py': '_migrated.py', '.java': '_migrated.java', '.php': '_migrated.php', '.cbl': '_migrated.py', '.cob': '_migrated.py'}
    for ext, new_ext in ext_map.items():
        if filename.lower().endswith(ext):
            filename = filename[:-len(ext)] + new_ext
            break
    write_audit_log("download", file.filename, "language=" + lang)
    return Response(
        content=migrated.encode('utf-8'),
        media_type='application/octet-stream',
        headers={"Content-Disposition": f'attachment; filename="{filename}"'}
    )'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")