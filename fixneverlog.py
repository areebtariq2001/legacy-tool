main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''_NEVER_LOG_PATTERNS = [
    re.compile(r"(sk_live|sk_test|AKIA|ghp_|xox[a-z]-)[A-Za-z0-9_\\-]{10,}"),
    re.compile(r"-----BEGIN (RSA |EC )?PRIVATE KEY-----"),
    re.compile(r"(password|secret|token|api.?key)\\s*[=:]\\s*['\\x22][^'\\x22]{6,}['\\x22]", re.IGNORECASE),
]'''

new = '''_NEVER_LOG_PATTERNS = [
    re.compile(r"(sk_live|sk_test|AKIA|ghp_|xox[a-z]-)[A-Za-z0-9_\\-]{10,}"),
    re.compile(r"-----BEGIN (RSA |EC )?PRIVATE KEY-----"),
    re.compile(r"(password|secret|token|api.?key)\\s*[=:]\\s*['\\x22][^'\\x22]{6,}['\\x22]", re.IGNORECASE),
    re.compile(r"://[^:/@\\s]+:[^@/\\s]+@[^\\s/]+"),  # DB/service connection strings embedding credentials (e.g. postgresql://user:pass@host)
    re.compile(r"Bearer\\s+[A-Za-z0-9\\-_.]{10,}", re.IGNORECASE),  # HTTP Authorization: Bearer <token> headers
]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXNEVERLOG-DONE")
else:
    print("FAILED - count was:", count)