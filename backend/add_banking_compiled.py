with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def detect_banking_patterns(source):'''
new = '''BANKING_PATTERNS_COMPILED = [(re.compile(p), label, note) for p, label, note in BANKING_PATTERNS]

def detect_banking_patterns(source):'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")