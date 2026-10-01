main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '_endpoint_identifier = ("token:" + _session_token) if _session_token else ("ip:" + client_ip)'
new = '_endpoint_identifier = "ip:" + client_ip  # always IP-based: an unvalidated client-supplied session-token would let an attacker bypass this limit simply by rotating the header value on each request'

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXTOKENBYPASS-DONE")
else:
    print("FAILED - count was:", count)