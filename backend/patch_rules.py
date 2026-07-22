with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        m = _re7.match(r"(if|elif)\s+(.+?):", stripped)
        m2 = _re7.match(r"(?:\}\s*)?(else\s+)?if\s*\((.+)\)\s*\{?", stripped) if not m else None
        condition = None
        if m:
            condition = m.group(2).strip()
        elif m2:
            condition = m2.group(2).strip()'''

new = '''        m = _re7.match(r"(if|elif)\s+(.+?):", stripped)
        m2 = _re7.match(r"(?:\}\s*)?(else\s+)?if\s*\((.+)\)\s*\{?", stripped) if not m else None
        m3 = _re7.match(r"(?i)IF\s+(.+?)\.?$", stripped) if (not m and not m2 and filename.lower().endswith((".cbl", ".cob"))) else None
        condition = None
        if m:
            condition = m.group(2).strip()
        elif m2:
            condition = m2.group(2).strip()
        elif m3:
            condition = m3.group(1).strip().rstrip(".")'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")