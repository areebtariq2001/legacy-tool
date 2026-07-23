with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("*"):
            continue'''

new = '''    import re as _seqre
    for raw_line in lines:
        line = raw_line.strip()
        seq_match = _seqre.match(r"^(\d{6})\s+(.*)$", line)
        if seq_match:
            line = seq_match.group(2)
        if not line or line.startswith("*"):
            continue'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")