with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = 'app = FastAPI('
new = '''_rate_limit_store = {}
import time as _rl_time

def _check_rate_limit(ip, max_requests=60, window_seconds=60):
    now = _rl_time.time()
    entry = _rate_limit_store.get(ip, [])
    entry = [t for t in entry if now - t < window_seconds]
    if len(entry) >= max_requests:
        return False
    entry.append(now)
    _rate_limit_store[ip] = entry
    return True

app = FastAPI('''

count = content.count(old)
print("Occurrences found:", count)
if count >= 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - trying alternate pattern")