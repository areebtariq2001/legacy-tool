with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    _ntn_var_pattern = re.compile(r"(?i)\\b(ntn|strn|tax.?number|tax.?registration)\\b")
    _length_check_pattern = re.compile(r"(?i)len\\([^)]*\\)\\s*[=!]=\\s*\\d+")
    _digit_check_pattern = re.compile(r"(?i)isdigit|isnumeric|\\\\d\\{\\d+\\}")
    findings = []
    ntn_functions_found = 0
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            func_source = ast.get_source_segment(source, node) or ""
            _code_only = chr(10).join(l for l in func_source.split(chr(10)) if not l.strip().startswith("#"))
            if not _ntn_var_pattern.search(_code_only):
                continue
            ntn_functions_found += 1
            has_length_check = bool(_length_check_pattern.search(_code_only))
            has_format_check = bool(_digit_check_pattern.search(_code_only))
            issues = []
            if not has_length_check:
                issues.append("No explicit length check found in this NTN/STRN-related function.")
            if not has_format_check:
                issues.append("No explicit numeric/digit-format validation found in this NTN/STRN-related function.")
            if issues:
                findings.append({"function": node.name, "line": node.lineno, "issues": issues})
    if ntn_functions_found == 0:'''

new = '''    _ntn_var_pattern = re.compile(r"(?i)\\b(ntn|strn|tax.?number|tax.?registration)\\b")
    _length_check_pattern = re.compile(r"(?i)len\\([^)]*\\)\\s*[=!]=\\s*\\d+")
    _digit_check_pattern = re.compile(r"(?i)isdigit|isnumeric|\\\\d\\{\\d+\\}")
    _check_patterns = [
        ("length", _length_check_pattern, "No explicit length check found in this NTN/STRN-related function."),
        ("format", _digit_check_pattern, "No explicit numeric/digit-format validation found in this NTN/STRN-related function."),
    ]
    _scan_result = _scan_functions_for_keyword_and_checks(source, filename, _ntn_var_pattern, _check_patterns)
    findings = _scan_result["findings"]
    ntn_functions_found = _scan_result["functions_found"]
    if ntn_functions_found == 0:'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("NTN-REFACTOR-SUCCESSFUL")
else:
    print("FAILED - aborting to be safe")