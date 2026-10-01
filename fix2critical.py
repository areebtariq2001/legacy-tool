main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: add missing urllib.parse import (near the top, next to other stdlib imports)
old1 = '_rate_limit_store = {}\nimport time'
new1 = '_rate_limit_store = {}\nimport time\nimport urllib.parse'
results["1_add_urllib_import"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: fix rate-limit endpoint keys to match actual routes
old2 = '''_ENDPOINT_SPECIFIC_LIMITS = {
    "/ai-migrate": (5, 60),
    "/scan-sensitive": (10, 60),
    "/generate-tests": (5, 60),
    "/login": (5, 300),
    "/register": (3, 300),
}'''
new2 = '''_ENDPOINT_SPECIFIC_LIMITS = {
    "/ai-migrate": (5, 60),
    "/scan-sensitive": (10, 60),
    "/generate-tests": (5, 60),
    "/auth/login": (5, 300),
    "/auth/register": (3, 300),
}'''
results["2_fix_endpoint_keys"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIX2CRITICAL-DONE")