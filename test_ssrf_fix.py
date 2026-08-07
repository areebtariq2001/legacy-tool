import re

pattern = r"^https://github\.com/[\w\-\.]+/[\w\-\.]+$"

test_urls = [
    "https://github.com/owner/repo",
    "https://github.com/../../internal-service/secret",
    "https://github.com/evil/repo#@internal.server.com",
    "http://github.com/owner/repo",
    "https://github.com/owner/repo/../../../etc",
]

for url in test_urls:
    matches = bool(re.match(pattern, url.rstrip("/")))
    print(url, "->", "ALLOWED" if matches else "BLOCKED")