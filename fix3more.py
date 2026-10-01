main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: has_key regex - match dotted-path identifiers like "self.cache", not just single words
old1 = "migrated = re.sub(r'(\\w+)\\.has_key\\(([^)]+)\\)', _safe_haskey_sub, migrated)"
new1 = "migrated = re.sub(r'((?:\\w+\\.)*\\w+)\\.has_key\\(([^)]+)\\)', _safe_haskey_sub, migrated)"
results["1_haskey_regex"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: remove the "jailbroken" false-positive-prone indicator (legitimate in mobile-security-analysis contexts)
old2 = '    "i am now unrestricted",\n    "jailbroken",\n]'
new2 = '    "i am now unrestricted",\n]'
results["2_remove_jailbroken_fp"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: reject ".." in GitHub owner/repo names (defense-in-depth against path-traversal-style input)
old3 = '    if not re.match(r"^[\\w.-]+$", owner) or not re.match(r"^[\\w.-]+$", repo):\n        return {"error": "Invalid owner or repo name in the URL - only letters, numbers, dots, hyphens, and underscores are allowed."}'
new3 = '    if not re.match(r"^[\\w.-]+$", owner) or not re.match(r"^[\\w.-]+$", repo) or ".." in owner or ".." in repo:\n        return {"error": "Invalid owner or repo name in the URL - only letters, numbers, dots, hyphens, and underscores are allowed."}'
results["3_reject_dotdot"] = content.count(old3)
content = content.replace(old3, new3, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIX3MORE-DONE")