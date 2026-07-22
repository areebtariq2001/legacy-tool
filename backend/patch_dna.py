with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    security_score = crypto.get("quantum_score", 100)'''

new = '''    security_score = crypto.get("quantum_score", 100)
    try:
        pii = detect_pii(source, filename)
        if pii.get("pii_findings"):
            security_score = max(0, security_score - len(pii.get("pii_findings", [])) * 10)
    except Exception:
        pass'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")