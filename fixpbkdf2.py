main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: _hash_password - bump to 600k iterations (OWASP-current), storing the count for future flexibility and backward-compat
old1 = '''def _hash_password(password, salt=None):
    if salt is None:
        salt = secrets.token_hex(16)
    pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), 200000).hex()
    return salt + "$" + pwd_hash'''
new1 = '''def _hash_password(password, salt=None, iterations=600000):
    if salt is None:
        salt = secrets.token_hex(16)
    pwd_hash = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt.encode("utf-8"), iterations).hex()
    return salt + "$" + str(iterations) + "$" + pwd_hash'''
results["1_hash_password"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: _verify_password - handle both old 2-part (salt$hash, implicitly 200k) and new 3-part (salt$iterations$hash) formats
old2 = '''def _verify_password(password, stored_hash):
    try:
        salt, _ = stored_hash.split("$", 1)
    except Exception:
        return False
    return hmac.compare_digest(_hash_password(password, salt), stored_hash)'''
new2 = '''def _verify_password(password, stored_hash):
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
results["2_verify_password"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: _DUMMY_HASH_FOR_TIMING - update to match new format so timing-attack mitigation stays consistent
old3 = '_DUMMY_HASH_FOR_TIMING = "0" * 32 + "$" + hashlib.pbkdf2_hmac("sha256", b"dummy_password_for_timing", ("0" * 32).encode("utf-8"), 200000).hex()'
new3 = '_DUMMY_HASH_FOR_TIMING = "0" * 32 + "$600000$" + hashlib.pbkdf2_hmac("sha256", b"dummy_password_for_timing", ("0" * 32).encode("utf-8"), 600000).hex()'
results["3_dummy_hash"] = content.count(old3)
content = content.replace(old3, new3, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXPBKDF2-DONE")