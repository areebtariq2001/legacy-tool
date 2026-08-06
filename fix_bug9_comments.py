with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    for pattern, label, severity in SENSITIVE_PATTERNS_COMPILED:
        count = 0
        line_nums = []
        for i, ln in enumerate(source_lines):
            _m = pattern.findall(ln)'''

new = '''    for pattern, label, severity in SENSITIVE_PATTERNS_COMPILED:
        count = 0
        line_nums = []
        for i, ln in enumerate(source_lines):
            if ln.strip().startswith(("#", "//")):
                continue
            _m = pattern.findall(ln)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")