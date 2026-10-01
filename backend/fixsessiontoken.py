main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''    _session_token = request.headers.get("x-session-token", "")
    if _session_token and len(_session_token) <= 200:
        if not _check_rate_limit_keyed(_token_rate_limit_store, "tok:" + _session_token, max_requests=90, window_seconds=60):
            return JSONResponse(
                content={"error": "Rate limit exceeded for this session. Please slow down and try again shortly."},
                status_code=429,
                headers={"Access-Control-Allow-Origin": allow_origin}
            )
    _path = request.url.path'''

new = '''    # NOTE: an earlier per-session-token rate limit here (keyed on the client-supplied
    # x-session-token header) has been removed - a client-controlled value can never be
    # a trustworthy rate-limiting key, since an attacker can simply send a fresh token
    # value on every request to reset their own limit, making that check pure security
    # theater. The IP-based global limit above and the IP-based per-endpoint limit below
    # are the checks that actually can't be bypassed by the client.
    _path = request.url.path'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXSESSIONTOKEN-DONE")
else:
    print("FAILED - count was:", count)