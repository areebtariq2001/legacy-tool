with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    def count_defs(code):
        funcs = 0
        classes = 0
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    funcs += 1
                elif isinstance(node, ast.ClassDef):
                    classes += 1
        except:
            pass
        return funcs, classes'''

new = '''    def count_defs(code):
        funcs = 0
        classes = 0
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    funcs += 1
                elif isinstance(node, ast.ClassDef):
                    classes += 1
        except Exception:
            funcs = len(re.findall(r"^\\s*def\\s+\\w+", code, re.MULTILINE))
            classes = len(re.findall(r"^\\s*class\\s+\\w+", code, re.MULTILINE))
        return funcs, classes'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")