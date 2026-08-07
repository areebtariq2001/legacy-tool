with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    calls_map = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            inner_calls = []
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call):
                    fname = None
                    if isinstance(sub.func, ast.Name):
                        fname = sub.func.id
                    elif isinstance(sub.func, ast.Attribute):
                        fname = sub.func.attr
                    if fname and fname in defined_functions and fname != node.name:
                        if fname not in inner_calls:
                            inner_calls.append(fname)
            calls_map[node.name] = inner_calls'''

new = '''    calls_map = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            inner_calls = []
            nested_defs = [s for s in ast.walk(node) if isinstance(s, ast.FunctionDef) and s is not node]
            nested_call_ids = set()
            for nd in nested_defs:
                for s2 in ast.walk(nd):
                    nested_call_ids.add(id(s2))
            for sub in ast.walk(node):
                if isinstance(sub, ast.Call) and id(sub) not in nested_call_ids:
                    fname = None
                    if isinstance(sub.func, ast.Name):
                        fname = sub.func.id
                    elif isinstance(sub.func, ast.Attribute):
                        fname = sub.func.attr
                    if fname and fname in defined_functions and fname != node.name:
                        if fname not in inner_calls:
                            inner_calls.append(fname)
            calls_map[node.name] = inner_calls'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")