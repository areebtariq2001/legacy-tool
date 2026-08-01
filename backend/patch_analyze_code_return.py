with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    if re.search(r'\\bexcept\\s+\\w+\\s*,', source):
        issues.append("old except syntax found - use 'except X as e'")
    return {"functions": functions, "classes": classes, "imports": imports, "issues": issues}'''

new = '''    if re.search(r'\\bexcept\\s+\\w+\\s*,', source):
        issues.append("old except syntax found - use 'except X as e'")
    if parse_failed:
        issues.insert(0, "Could not fully parse with Python's AST (likely Python 2-only syntax) - showing pattern-based findings below; function/class detection may be incomplete.")
    return {"functions": functions, "classes": classes, "imports": imports, "issues": issues, "ast_parse_failed": parse_failed}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")