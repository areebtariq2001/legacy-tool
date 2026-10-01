main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _verify_security_log_integrity():
    with _security_log_lock:
        _chronological = list(reversed(_security_log))
        _expected_prev = "0" * 64
        for _entry in _chronological:'''
new = '''def _verify_security_log_integrity():
    with _security_log_lock:
        _chronological = list(reversed(_security_log))
        # The log is capped at 200 entries (del _security_log[200:]) to bound memory,
        # so after more than 200 events the oldest surviving entry's own prev_hash
        # legitimately points to an older, now-discarded entry rather than the
        # genesis "0"*64 value. Seed verification from that entry's own prev_hash
        # instead of assuming "0"*64, so integrity is checked over the retained
        # window rather than falsely flagging normal log rotation as tampering.
        _expected_prev = _chronological[0]["prev_hash"] if _chronological else "0" * 64
        for _entry in _chronological:'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXSECLOG-DONE")
else:
    print("FAILED - count was:", count)