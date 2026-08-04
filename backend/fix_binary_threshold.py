with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    printable = sum(1 for c in source[:1000] if c.isprintable() or c in "\\n\\r\\t ")
    if len(source) > 0 and printable / min(len(source), 1000) < 0.7:
        return None, "File does not appear to be text/code (may be binary)."'''

new = '''    sample = source[:2000]
    printable = sum(1 for c in sample if c.isprintable() or c in "\\n\\r\\t \\x0c")
    if len(sample) > 0 and printable / len(sample) < 0.5:
        return None, "File does not appear to be text/code (may be binary)."'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")