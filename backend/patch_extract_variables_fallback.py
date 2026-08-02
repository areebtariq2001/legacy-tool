with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def extract_variables(code):
    names = set()
    try:
        tree = ast.parse(code)
    except:
        return names'''

new = '''def extract_variables(code):
    names = set()
    try:
        tree = ast.parse(code)
    except Exception:
        for _m in re.finditer(r"^\\s*(\\w+)\\s*=[^=]", code, re.MULTILINE):
            names.add(_m.group(1))
        for _m in re.finditer(r"\\bdef\\s+\\w+\\s*\\(([^)]*)\\)", code):
            for _param in _m.group(1).split(","):
                _p = _param.strip().split("=")[0].strip()
                if _p and _p.isidentifier():
                    names.add(_p)
        for _m in re.finditer(r"\\bdef\\s+(\\w+)\\s*\\(", code):
            names.add(_m.group(1))
        return names - _PY_BUILTINS'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")