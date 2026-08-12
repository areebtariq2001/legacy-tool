with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = '''        webhook_secret = os.environ.get("GITHUB_WEBHOOK_SECRET", "")
        if webhook_secret:
            signature = request.headers.get("x-hub-signature-256", "")
            expected = "sha256=" + hmac.new(webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()
            if not hmac.compare_digest(expected, signature):
                return JSONResponse(status_code=401, content={"error": "Invalid webhook signature"})'''
new = '''        webhook_secret = os.environ.get("GITHUB_WEBHOOK_SECRET", "")
        if not webhook_secret:
            return JSONResponse(status_code=401, content={"error": "Webhook not configured - GITHUB_WEBHOOK_SECRET is not set on the server"})
        signature = request.headers.get("x-hub-signature-256", "")
        expected = "sha256=" + hmac.new(webhook_secret.encode(), raw_body, hashlib.sha256).hexdigest()
        if not hmac.compare_digest(expected, signature):
            return JSONResponse(status_code=401, content={"error": "Invalid webhook signature"})'''
count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")