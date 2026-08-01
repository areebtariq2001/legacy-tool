with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''r"(?i)(password|passwd|pwd|api_key|secret)\\s*=\\s*[\\x22\\x27][^\\x22\\x27]{3,}[\\x22\\x27]"'''

new = '''r"(?i)(password|passwd|pwd|pass|api_key|apikey|secret)\\s*=\\s*[\\x22\\x27][^\\x22\\x27]{3,}[\\x22\\x27]"'''

count = content.count(old)
print("Occurrences found:", count)
if count >= 1:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY -", count, "occurrence(s) fixed")
else:
    print("FAILED - aborting to be safe")