with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def funcs_has_no_hints(source):
    import re as _re2
    defs = _re2.findall(r"def\\s+\\w+\\s*\\(([^)]*)\\)", source)
    if not defs:
        return False
    for d in defs:
        if ":" in d:
            return False
    return True'''

new = '''def funcs_has_no_hints(source):
    _re2 = re
    defs = _re2.findall(r"def\\s+\\w+\\s*\\(([\\s\\S]*?)\\)\\s*(?:->|:)", source)
    defs = [d for d in defs if d.strip()]
    if not defs:
        return False
    _hint_pattern = _re2.compile(r"\\b\\w+\\s*:\\s*[\\w\\[\\]\\.\\'\\\"]+")
    for d in defs:
        if not _hint_pattern.search(d):
            return True
    return False'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")