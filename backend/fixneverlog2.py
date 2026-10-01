main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''    re.compile(r"://[^:/@\\s]+:[^@/\\s]+@[^\\s/]+"),  # DB/service connection strings embedding credentials (e.g. postgresql://user:pass@host)
    re.compile(r"Bearer\\s+[A-Za-z0-9\\-_.]{10,}", re.IGNORECASE),  # HTTP Authorization: Bearer <token> headers
]'''

new = '''    re.compile(r"://[^:/@\\s]+:[^@/\\s]+@[^\\s/]+"),  # DB/service connection strings embedding credentials (e.g. postgresql://user:pass@host)
    re.compile(r"Bearer\\s+[A-Za-z0-9\\-_.]{10,}", re.IGNORECASE),  # HTTP Authorization: Bearer <token> headers
    re.compile(r"gsk_[A-Za-z0-9]{10,}"),  # Groq API keys - this app's own AI provider
    re.compile(r"eyJ[A-Za-z0-9_\\-]{10,}\\.[A-Za-z0-9_\\-]{10,}\\.[A-Za-z0-9_\\-]{5,}"),  # JWT tokens (header.payload.signature, base64url)
    re.compile(r"(password|secret|token|api.?key)\\s*[=:]\\s*[A-Za-z0-9_\\-]{6,}", re.IGNORECASE),  # unquoted key=value (e.g. query-string style api_key=abc123), in addition to the quoted-value pattern above
]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXNEVERLOG2-DONE")
else:
    print("FAILED - count was:", count)