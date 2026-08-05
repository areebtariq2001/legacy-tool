with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.get("/audit-log-json")
def get_audit_log_json():
    entries = []
    with _stats_lock:
        raw_lines = list(_in_memory_audit_log)
    for line in raw_lines:
        line = line.strip()
        if not line:
            continue
        entry = {"raw": line}
        try:
            if line.startswith("["):
                entry["timestamp"] = line.split("]")[0][1:]
            if "action=" in line:
                entry["action"] = line.split("action=")[1].split(" |")[0].strip()
            if "file=" in line:
                entry["file"] = line.split("file=")[1].split(" |")[0].strip()
            if "result=" in line:
                entry["result"] = line.split("result=")[1].strip()
        except Exception as e:
            entry["parse_error"] = str(e)
        entries.append(entry)
    return {"audit_ready": True, "total_entries": len(entries), "entries": entries[:100]}'''

new = '''@app.get("/audit-log-json")
def get_audit_log_json(request: Request):
    if not _check_admin_auth(request):
        return JSONResponse(status_code=401, content={"error": "Unauthorized - valid x-admin-key header required"})
    with _stats_lock:
        raw_entries = list(_in_memory_audit_log)
    entries = []
    for e in raw_entries:
        if isinstance(e, dict):
            entries.append(dict(e))
        else:
            entries.append({"raw": str(e)})
    return {"audit_ready": True, "total_entries": len(entries), "entries": entries[:100]}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")