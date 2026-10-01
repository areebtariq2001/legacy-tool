main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _check_rate_limit(ip, max_requests=60, window_seconds=60):
    now = time.time()
    entry = _rate_limit_store.get(ip, [])
    entry = [t for t in entry if now - t < window_seconds]
    if len(entry) >= max_requests:
        _rate_limit_store[ip] = entry
        _record_security_event("rate_limit_violation", ip, f"exceeded {max_requests} requests per {window_seconds}s")
        return False
    entry.append(now)
    _rate_limit_store[ip] = entry
    if len(_rate_limit_store) > 5000:
        _cutoff = now - window_seconds
        for _k in list(_rate_limit_store.keys()):
            if not _rate_limit_store[_k] or max(_rate_limit_store[_k]) < _cutoff:
                del _rate_limit_store[_k]
    return True'''

new = '''_rate_limit_lock = threading.Lock()


def _check_rate_limit(ip, max_requests=60, window_seconds=60):
    now = time.time()
    with _rate_limit_lock:
        entry = _rate_limit_store.get(ip, [])
        entry = [t for t in entry if now - t < window_seconds]
        if len(entry) >= max_requests:
            _rate_limit_store[ip] = entry
            _record_security_event("rate_limit_violation", ip, f"exceeded {max_requests} requests per {window_seconds}s")
            return False
        entry.append(now)
        _rate_limit_store[ip] = entry
        if len(_rate_limit_store) > 5000:
            _cutoff = now - window_seconds
            for _k in list(_rate_limit_store.keys()):
                if not _rate_limit_store[_k] or max(_rate_limit_store[_k]) < _cutoff:
                    del _rate_limit_store[_k]
        return True'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXRATELIMIT-DONE")
else:
    print("FAILED - count was:", count)