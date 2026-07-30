with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''STATS_FILE = "stats.json"

def load_stats():
    try:
        with open(STATS_FILE, "r") as f:
            return json.load(f)
    except:
        return {"total_files": 0, "total_migrations": 0, "total_analyses": 0, "logs": []}

def save_stats(stats):
    try:
        with open(STATS_FILE, "w") as f:
            json.dump(stats, f)
    except:
        pass

def write_audit_log(action, filename, result_summary):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_line = f"[{timestamp}] action={action} | file={filename} | result={result_summary}\\n"
        with open("audit_log.txt", "a", encoding="utf-8") as f:
            f.write(log_line)
    except:
        pass

def track_usage(action, filename):
    stats = load_stats()
    stats["total_files"] += 1
    if "migrate" in action:
        stats["total_migrations"] += 1
    elif "analyze" in action:
        stats["total_analyses"] += 1
    stats["logs"].insert(0, {
        "action": action,
        "filename": filename,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })
    stats["logs"] = stats["logs"][:50]
    save_stats(stats)'''

new = '''import threading
_stats_lock = threading.Lock()
_in_memory_stats = {"total_files": 0, "total_migrations": 0, "total_analyses": 0, "logs": []}
_in_memory_audit_log = []

def load_stats():
    with _stats_lock:
        return dict(_in_memory_stats)

def save_stats(stats):
    with _stats_lock:
        _in_memory_stats.update(stats)

def write_audit_log(action, filename, result_summary):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with _stats_lock:
            _in_memory_audit_log.insert(0, f"[{timestamp}] action={action} | file={filename} | result={result_summary}")
            del _in_memory_audit_log[50:]
    except:
        pass

def track_usage(action, filename):
    with _stats_lock:
        _in_memory_stats["total_files"] += 1
        if "migrate" in action:
            _in_memory_stats["total_migrations"] += 1
        elif "analyze" in action:
            _in_memory_stats["total_analyses"] += 1
        _in_memory_stats["logs"].insert(0, {
            "action": action,
            "filename": filename,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        del _in_memory_stats["logs"][50:]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")