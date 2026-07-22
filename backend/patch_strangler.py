with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    elif filename.lower().endswith(".php"):
        import re as _sfre
        funcs = _sfre.findall(r"function\s+(\w+)\s*\(", source)
    else:'''

new = '''    elif filename.lower().endswith(".php"):
        import re as _sfre
        funcs = _sfre.findall(r"function\s+(\w+)\s*\(", source)
    elif filename.lower().endswith((".cbl", ".cob")):
        import re as _sfre
        funcs = _sfre.findall(r"(?m)^\s{0,7}([\w-]+)\.\s*$", source)
    else:'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")