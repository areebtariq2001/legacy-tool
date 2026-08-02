with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        try:
            tree = ast.parse(source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_lines = (node.end_lineno - node.lineno) if hasattr(node, "end_lineno") else 0
                    if func_lines > 50:
                        smells.append({"type": "Long Function", "location": "Function " + node.name + " (line " + str(node.lineno) + ")", "detail": "Function is " + str(func_lines) + " lines long - consider splitting into smaller functions.", "severity": "Medium"})
        except Exception:
            pass'''

new = '''        try:
            tree = ast.parse(source)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_lines = (node.end_lineno - node.lineno) if hasattr(node, "end_lineno") else 0
                    if func_lines > 50:
                        smells.append({"type": "Long Function", "location": "Function " + node.name + " (line " + str(node.lineno) + ")", "detail": "Function is " + str(func_lines) + " lines long - consider splitting into smaller functions.", "severity": "Medium"})
        except Exception:
            _def_positions = [(m.start(), m.group(1)) for m in re.finditer(r"^def\\s+(\\w+)", source, re.MULTILINE)]
            for idx, (pos, fname) in enumerate(_def_positions):
                start_line = source[:pos].count(chr(10)) + 1
                end_pos = _def_positions[idx + 1][0] if idx + 1 < len(_def_positions) else len(source)
                func_lines_est = source[pos:end_pos].count(chr(10))
                if func_lines_est > 50:
                    smells.append({"type": "Long Function", "location": "Function " + fname + " (line " + str(start_line) + ", approximate - could not fully parse)", "detail": "Function is approximately " + str(func_lines_est) + " lines long - consider splitting into smaller functions.", "severity": "Medium"})'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")