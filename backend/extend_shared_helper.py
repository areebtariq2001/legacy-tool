with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _scan_functions_for_keyword_and_checks(source, filename, keyword_pattern, check_patterns):
    if not filename.lower().endswith(".py"):
        return {"supported": False, "functions_found": 0, "findings": []}
    try:
        tree = ast.parse(source)
    except Exception:
        return {"supported": False, "functions_found": 0, "findings": [], "parse_error": True}
    findings = []
    functions_found = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_source = ast.get_source_segment(source, node) or ""
            _code_only = chr(10).join(l for l in func_source.split(chr(10)) if not l.strip().startswith("#"))
            if not keyword_pattern.search(_code_only):
                continue
            functions_found += 1'''

new = '''def _scan_functions_for_keyword_and_checks(source, filename, keyword_pattern, check_patterns, context_filter=None):
    if not filename.lower().endswith(".py"):
        return {"supported": False, "functions_found": 0, "findings": []}
    try:
        tree = ast.parse(source)
    except Exception:
        return {"supported": False, "functions_found": 0, "findings": [], "parse_error": True}
    findings = []
    functions_found = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_source = ast.get_source_segment(source, node) or ""
            _code_only = chr(10).join(l for l in func_source.split(chr(10)) if not l.strip().startswith("#"))
            if not keyword_pattern.search(_code_only):
                continue
            if context_filter is not None and not context_filter(func_source):
                continue
            functions_found += 1'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("SHARED-HELPER-EXTENDED")
else:
    print("FAILED - aborting to be safe")