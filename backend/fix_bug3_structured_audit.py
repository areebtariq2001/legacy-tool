with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''        with _stats_lock:
            _in_memory_audit_log.insert(0, f"[{timestamp}] action={action} | file={filename} | result={result_summary}")
            del _in_memory_audit_log[50:]
    except Exception:
        pass'''

new1 = '''        with _stats_lock:
            _in_memory_audit_log.insert(0, {"timestamp": timestamp, "action": action, "file": filename, "result": result_summary})
            del _in_memory_audit_log[50:]
    except Exception:
        pass'''

count1 = content.count(old1)
print("Fix 1 (write_audit_log storage) occurrences:", count1)
if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Fix 1 PATCHED")

old2 = '''@app.get("/audit-log")
def get_audit_log(request: Request):
    if not _check_admin_auth(request):
        return JSONResponse(status_code=401, content={"error": "Unauthorized - valid x-admin-key header required"})
    with _stats_lock:
        all_entries = list(_in_memory_audit_log)
        recent = all_entries[:50]
    return {"total_entries": len(all_entries), "recent": recent}'''

new2 = '''@app.get("/audit-log")
def get_audit_log(request: Request):
    if not _check_admin_auth(request):
        return JSONResponse(status_code=401, content={"error": "Unauthorized - valid x-admin-key header required"})
    with _stats_lock:
        all_entries = list(_in_memory_audit_log)
        recent = all_entries[:50]
    recent_display = ["[" + e.get("timestamp","") + "] action=" + e.get("action","") + " | file=" + e.get("file","") + " | result=" + e.get("result","") if isinstance(e, dict) else str(e) for e in recent]
    return {"total_entries": len(all_entries), "recent": recent_display}'''

count2 = content.count(old2)
print("Fix 2 (/audit-log display) occurrences:", count2)
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Fix 2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")