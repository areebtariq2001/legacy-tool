with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = '''def _check_admin_auth(request: Request):
    required_key = os.environ.get("ADMIN_API_KEY", "")
    if not required_key:
        return True
    provided_key = request.headers.get("x-admin-key", "")
    return provided_key == required_key'''
new = '''def _check_admin_auth(request: Request):
    required_key = os.environ.get("ADMIN_API_KEY", "")
    if not required_key:
        return False
    provided_key = request.headers.get("x-admin-key", "")
    return hmac.compare_digest(provided_key, required_key)'''
count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")