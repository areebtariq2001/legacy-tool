with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''(r"\\b(?:[0-9]{1,3}\\.){3}[0-9]{1,3}\\b", "Hardcoded IP address"), (r"(?i)(api_key|apikey|secret|token)\\s*=\\s*[\\"\\x27][^\\"\\x27]+[\\"\\x27]", "Hardcoded API key/secret")'''
new = '''(r"\\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\b", "Hardcoded IP address"), (r"(?i)(api_key|apikey|secret|token)\\s*=\\s*[\\"\\x27][^\\"\\x27]+[\\"\\x27]", "Hardcoded API key/secret")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")