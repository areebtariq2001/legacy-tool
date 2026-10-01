main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if not row:
            _verify_password(password, _DUMMY_HASH_FOR_TIMING)
            _attempts.append(_now)
            _failed_login_attempts[email] = _attempts
            return {"success": False, "error": "Invalid email or password"}
        if not _verify_password(password, row[1]):
            _attempts.append(_now)
            _failed_login_attempts[email] = _attempts
            return {"success": False, "error": "Invalid email or password"}
        _failed_login_attempts.pop(email, None)'''

new = '''        if not row:
            _verify_password(password, _DUMMY_HASH_FOR_TIMING)
            with _login_attempts_lock:
                _attempts.append(_now)
                _failed_login_attempts[email] = _attempts
            return {"success": False, "error": "Invalid email or password"}
        if not _verify_password(password, row[1]):
            with _login_attempts_lock:
                _attempts.append(_now)
                _failed_login_attempts[email] = _attempts
            return {"success": False, "error": "Invalid email or password"}
        with _login_attempts_lock:
            _failed_login_attempts.pop(email, None)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("COMPLETE-LOGIN-LOCK-DONE")
else:
    print("FAILED - count was:", count)