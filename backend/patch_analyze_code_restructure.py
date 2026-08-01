with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def analyze_code(source):
    try:
        tree = ast.parse(source)
    except:
        return {"functions": [], "classes": [], "imports": [], "issues": ["Could not parse - this analysis only supports valid Python 3 code. Non-Python files will show this."]}
    functions, classes, imports, issues = [], [], [], []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
        elif isinstance(node, ast.ClassDef):
            classes.append(node.name)
        elif isinstance(node, ast.Import):
            for a in node.names:
                imports.append(a.name)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.append(node.module)
    py_issue_checks = ['''

new = '''def analyze_code(source):
    functions, classes, imports, issues = [], [], [], []
    parse_failed = False
    try:
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
            elif isinstance(node, ast.ClassDef):
                classes.append(node.name)
            elif isinstance(node, ast.Import):
                for a in node.names:
                    imports.append(a.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imports.append(node.module)
    except Exception:
        parse_failed = True
        func_matches = re.findall(r"^\\s*def\\s+(\\w+)", source, re.MULTILINE)
        functions.extend(func_matches)
        class_matches = re.findall(r"^\\s*class\\s+(\\w+)", source, re.MULTILINE)
        classes.extend(class_matches)
    py_issue_checks = ['''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")