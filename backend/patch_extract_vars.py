with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def extract_variables(code):
    names = set()
    try:
        tree = ast.parse(code)
    except:
        return names
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            names.add(node.id)'''

new = '''_PY_BUILTINS = set(dir(__builtins__)) if isinstance(__builtins__, type(__builtins__)) else set(vars(__builtins__).keys())
_PY_BUILTINS |= {"True", "False", "None", "self", "cls"}

def extract_variables(code):
    names = set()
    try:
        tree = ast.parse(code)
    except:
        return names
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            if node.id not in _PY_BUILTINS:
                names.add(node.id)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")