with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''@app.get("/audit-log")
def get_audit_log():
    try:
        with open("audit_log.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
        return {"total_entries": len(lines), "recent": lines[-50:]}
    except:
        return {"total_entries": 0, "recent": []}'''

new1 = '''@app.get("/audit-log")
def get_audit_log():
    with _stats_lock:
        recent = list(_in_memory_audit_log[:50])
    return {"total_entries": len(recent), "recent": recent}'''

count1 = content.count(old1)
print("Endpoint 1 occurrences:", count1)

old2_start = '''@app.get("/audit-log-json")
def get_audit_log_json():
    entries = []
    try:
        with open("audit_log.txt", "r", encoding="utf-8") as f:
            for line in f:
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
                except:
                    pass
                entries.append(entry)
        return {"audit_ready": True, "total_entries": len(entries), "entries": entries[-100:]}
    except:
        return {"audit_ready": True, "total_entries": 0, "entries": []}'''

new2 = '''@app.get("/audit-log-json")
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
        except:
            pass
        entries.append(entry)
    return {"audit_ready": True, "total_entries": len(entries), "entries": entries[:100]}'''

count2 = content.count(old2_start)
print("Endpoint 2 occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Endpoint 1 PATCHED")
if count2 == 1:
    content = content.replace(old2_start, new2, 1)
    print("Endpoint 2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")