with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.get("/stats")
def get_stats():
    return load_stats()

@app.get("/audit-log")
def get_audit_log():
    with _stats_lock:
        all_entries = list(_in_memory_audit_log)
        recent = all_entries[:50]
    return {"total_entries": len(all_entries), "recent": recent}'''

new = '''def _check_admin_auth(request: Request):
    required_key = os.environ.get("ADMIN_API_KEY", "")
    if not required_key:
        return True
    provided_key = request.headers.get("x-admin-key", "")
    return provided_key == required_key

@app.get("/stats")
def get_stats(request: Request):
    if not _check_admin_auth(request):
        return JSONResponse(status_code=401, content={"error": "Unauthorized - valid x-admin-key header required"})
    return load_stats()

@app.get("/audit-log")
def get_audit_log(request: Request):
    if not _check_admin_auth(request):
        return JSONResponse(status_code=401, content={"error": "Unauthorized - valid x-admin-key header required"})
    with _stats_lock:
        all_entries = list(_in_memory_audit_log)
        recent = all_entries[:50]
    return {"total_entries": len(all_entries), "recent": recent}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")