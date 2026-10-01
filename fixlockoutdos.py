main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: login_user - accept ip, key the hard-block lockout by email+ip so an attacker
# can't lock a victim out from every IP just by knowing their email; the short-term
# progressive-delay backoff stays keyed purely by email (this bounds the DoS blast
# radius to the attacker's own IP for the hard block, while still slowing down
# a single-IP brute-force attempt against the account).
old1 = '''def login_user(email, password):
    email = (email or "").strip().lower()
    _now = time.time()
    with _login_attempts_lock:
        if len(_failed_login_attempts) > 5000:
            _stale = [e for e, ts in _failed_login_attempts.items() if not any(_now - t < 900 for t in ts)]
            for e in _stale:
                _failed_login_attempts.pop(e, None)
        _attempts = [t for t in _failed_login_attempts.get(email, []) if _now - t < 900]
        _attempt_count = len(_attempts)
        if _attempt_count >= 5:
            return {"success": False, "error": "Too many failed login attempts for this account. Please try again in 15 minutes."}
        if _attempt_count > 0:
            _required_wait = {1: 2, 2: 5, 3: 15, 4: 60}.get(_attempt_count, 0)
            _since_last = _now - _attempts[-1]
            if _since_last < _required_wait:
                return {"success": False, "error": f"Please wait {round(_required_wait - _since_last)} more second(s) before trying again."}
        _failed_login_attempts[email] = _attempts + [_now]'''

new1 = '''def login_user(email, password, ip="unknown"):
    email = (email or "").strip().lower()
    _now = time.time()
    _lockout_key = email + "|" + ip
    with _login_attempts_lock:
        if len(_failed_login_attempts) > 5000:
            _stale = [k for k, ts in _failed_login_attempts.items() if not any(_now - t < 900 for t in ts)]
            for k in _stale:
                _failed_login_attempts.pop(k, None)
        _attempts = [t for t in _failed_login_attempts.get(_lockout_key, []) if _now - t < 900]
        _attempt_count = len(_attempts)
        if _attempt_count >= 5:
            return {"success": False, "error": "Too many failed login attempts. Please try again in 15 minutes."}
        if _attempt_count > 0:
            _required_wait = {1: 2, 2: 5, 3: 15, 4: 60}.get(_attempt_count, 0)
            _since_last = _now - _attempts[-1]
            if _since_last < _required_wait:
                return {"success": False, "error": f"Please wait {round(_required_wait - _since_last)} more second(s) before trying again."}
        _failed_login_attempts[_lockout_key] = _attempts + [_now]'''
results["1_lockout_key"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: pop the lockout key (not bare email) on success
old2 = '''        with _login_attempts_lock:
            _failed_login_attempts.pop(email, None)
        user_id = row[0]'''
new2 = '''        with _login_attempts_lock:
            _failed_login_attempts.pop(_lockout_key, None)
        user_id = row[0]'''
results["2_pop_on_success"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: endpoint passes real client IP
old3 = '''@app.post("/auth/login")
async def auth_login_endpoint(req: AuthRequest):
    result = login_user(req.email, req.password)'''
new3 = '''@app.post("/auth/login")
async def auth_login_endpoint(req: AuthRequest, request: Request):
    result = login_user(req.email, req.password, ip=_get_client_ip(request))'''
results["3_endpoint_pass_ip"] = content.count(old3)
content = content.replace(old3, new3, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXLOCKOUTDOS-DONE")