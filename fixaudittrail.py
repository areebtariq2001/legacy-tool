main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old = '''def write_audit_log(action, filename, result_summary):
    global _audit_log_failure_count
    result_summary = safe_log_message(result_summary)
    try:
        audit_blockchain.add_block(action, filename, "anonymous", "unknown", result_summary)
    except Exception:
        pass
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = _get_db_connection()
        if conn:
            cur = None
            try:
                cur = conn.cursor()
                cur.execute("INSERT INTO usage_log (action, filename, result_summary) VALUES (%s, %s, %s)", (action, filename, result_summary))
                conn.commit()
                return
            except Exception:
                pass
            finally:
                if cur:
                    cur.close()
                conn.close()
        with _stats_lock:
            _in_memory_audit_log.insert(0, {"timestamp": timestamp, "action": action, "file": filename, "result": result_summary})
            del _in_memory_audit_log[50:]
    except Exception:
        _audit_log_failure_count += 1'''

new = '''def write_audit_log(action, filename, result_summary, user_email=None, ip=None):
    global _audit_log_failure_count
    result_summary = safe_log_message(result_summary)
    _user_email = user_email or "anonymous"
    _ip = ip or "unknown"
    try:
        audit_blockchain.add_block(action, filename, _user_email, _ip, result_summary)
    except Exception:
        pass
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = _get_db_connection()
        if conn:
            cur = None
            try:
                cur = conn.cursor()
                cur.execute("ALTER TABLE usage_log ADD COLUMN IF NOT EXISTS user_email TEXT")
                cur.execute("ALTER TABLE usage_log ADD COLUMN IF NOT EXISTS ip TEXT")
                cur.execute("INSERT INTO usage_log (action, filename, result_summary, user_email, ip) VALUES (%s, %s, %s, %s, %s)", (action, filename, result_summary, _user_email, _ip))
                conn.commit()
                return
            except Exception:
                pass
            finally:
                if cur:
                    cur.close()
                conn.close()
        with _stats_lock:
            _in_memory_audit_log.insert(0, {"timestamp": timestamp, "action": action, "file": filename, "result": result_summary, "user_email": _user_email, "ip": _ip})
            del _in_memory_audit_log[50:]
    except Exception:
        _audit_log_failure_count += 1'''

results["1_write_audit_log_signature"] = content.count(old)
content = content.replace(old, new, 1)

# Update the certificate-issuance call (which now has real auth) to pass real reviewer email
old2 = 'write_audit_log("issue-certificate", _filename, f"cert issued: {cert[\'certificate_id\']}")'
new2 = 'write_audit_log("issue-certificate", _filename, f"cert issued: {cert[\'certificate_id\']}", user_email=_reviewer_email)'
results["2_cert_call_real_email"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXAUDITTRAIL-DONE")