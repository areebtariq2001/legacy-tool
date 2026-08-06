with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def scan_sensitive_data(source):'''
new = '''SENSITIVE_PATTERNS_COMPILED = [(re.compile(p), label, sev) for p, label, sev in SENSITIVE_PATTERNS]

def scan_sensitive_data(source):'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")