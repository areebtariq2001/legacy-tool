main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _verify_password(password, stored_hash):
    try:
        parts = stored_hash.split("$")
        if len(parts) == 3:
            salt, iterations_str, _ = parts
            iterations = int(iterations_str)
        elif len(parts) == 2:
            salt, _ = parts
            iterations = 200000  # legacy format from before the iteration count was stored - preserved for backward compatibility with existing password hashes
        else:
            return False
    except Exception:
        return False
    return hmac.compare_digest(_hash_password(password, salt, iterations), stored_hash)'''

new = '''def _verify_password(password, stored_hash):
    try:
        parts = stored_hash.split("$")
        if len(parts) == 3:
            salt, iterations_str, expected_hash = parts
            iterations = int(iterations_str)
        elif len(parts) == 2:
            salt, expected_hash = parts
            iterations = 200000  # legacy format from before the iteration count was stored - preserved for backward compatibility with existing password hashes
        else:
            return False
    except Exception:
        return False
    computed_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations).hex()
    return hmac.compare_digest(computed_hash, expected_hash)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXPBKDF2V2-DONE")
else:
    print("FAILED - count was:", count)