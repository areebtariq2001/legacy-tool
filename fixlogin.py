main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: record the attempt IMMEDIATELY (optimistically) inside the first lock, before DB verification
old1 = '''        _attempt_count = len(_attempts)
        if _attempt_count >= 5:
            return {"success": False, "error": "Too many failed login attempts for this account. Please try again in 15 minutes."}
        if _attempt_count > 0:
            _required_wait = {1: 2, 2: 5, 3: 15, 4: 60}.get(_attempt_count, 0)
            _since_last = _now - _attempts[-1]
            if _since_last < _required_wait:
                return {"success": False, "error": f"Please wait {round(_required_wait - _since_last)} more second(s) before trying again."}'''
new1 = '''        _attempt_count = len(_attempts)
        if _attempt_count >= 5:
            return {"success": False, "error": "Too many failed login attempts for this account. Please try again in 15 minutes."}
        if _attempt_count > 0:
            _required_wait = {1: 2, 2: 5, 3: 15, 4: 60}.get(_attempt_count, 0)
            _since_last = _now - _attempts[-1]
            if _since_last < _required_wait:
                return {"success": False, "error": f"Please wait {round(_required_wait - _since_last)} more second(s) before trying again."}
        _failed_login_attempts[email] = _attempts + [_now]'''
results["1_record_upfront"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: remove the now-redundant later append in the "no such user" branch
old2 = '''        if not row:
            _verify_password(password, _DUMMY_HASH_FOR_TIMING)
            with _login_attempts_lock:
                _attempts.append(_now)
                _failed_login_attempts[email] = _attempts
            write_audit_log("login-failed", email, "invalid credentials")
            return {"success": False, "error": "Invalid email or password"}'''
new2 = '''        if not row:
            _verify_password(password, _DUMMY_HASH_FOR_TIMING)
            write_audit_log("login-failed", email, "invalid credentials")
            return {"success": False, "error": "Invalid email or password"}'''
results["2_remove_redundant_append_1"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: remove the now-redundant later append in the "wrong password" branch
old3 = '''        if not _verify_password(password, row[1]):
            with _login_attempts_lock:
                _attempts.append(_now)
                _failed_login_attempts[email] = _attempts
            write_audit_log("login-failed", email, "invalid credentials")
            return {"success": False, "error": "Invalid email or password"}'''
new3 = '''        if not _verify_password(password, row[1]):
            write_audit_log("login-failed", email, "invalid credentials")
            return {"success": False, "error": "Invalid email or password"}'''
results["3_remove_redundant_append_2"] = content.count(old3)
content = content.replace(old3, new3, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXLOGIN-DONE")