with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    try:
        tree = ast.parse(source)
        funcs = len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
        classes = len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)])
        parseable = True
    except Exception:
        if filename.lower().endswith(".php"):
            funcs = len(_re2.findall(r"function\\s+\\w+\\s*\\(", source))
            classes = len(_re2.findall(r"\\bclass\\s+\\w+", source))
        elif filename.lower().endswith((".cbl",".cob")):
            funcs = len(_re2.findall(r"(?mi)^(?:\\d{6}\\s+)?(?!END-)[\\w-]+\\.\\s*$", source))
            classes = 0
        elif filename.lower().endswith(".java"):
            funcs = len(_re2.findall(r"(?:public|private|protected)\\s+(?:static\\s+)?(?:synchronized\\s+)?[\\w<>\\[\\]]+\\s+\\w+\\s*\\([^)]*\\)\\s*(?:throws\\s+[\\w,\\s]+)?\\s*\\{", source))
            classes = len(_re2.findall(r"\\bclass\\s+\\w+", source))
        else:
            funcs = len(_re2.findall(r"def ", source)); classes = len(_re2.findall(r"class ", source))
        parseable = False
    security_hits = len(_re2.findall(r"(?i)(eval|exec|md5|sha1|password|verify=False|shell=True)", source))
    findings = []
    if not parseable and filename.lower().endswith(".py"): findings.append("Contains Python 2-only syntax - AST parser has partial visibility here; this is typically auto-fixed during migration, not a blocker")
    if security_hits > 0: findings.append(str(security_hits) + " potential security/compliance issue(s) detected")
    if len(lines) > 300: findings.append("Large file (" + str(len(lines)) + " lines) - higher migration effort")
    if not findings: findings.append("No major blockers detected - code appears in reasonable shape")
    health = 100 - (0 if parseable else 30) - min(security_hits*10, 40) - (10 if len(lines) > 300 else 0)'''

new = '''    _is_python_file = not (filename.lower().endswith((".php", ".java", ".cbl", ".cob")))
    try:
        tree = ast.parse(source)
        funcs = len([n for n in ast.walk(tree) if isinstance(n, ast.FunctionDef)])
        classes = len([n for n in ast.walk(tree) if isinstance(n, ast.ClassDef)])
        parseable = True
    except Exception:
        if filename.lower().endswith(".php"):
            funcs = len(_re2.findall(r"function\\s+\\w+\\s*\\(", source))
            classes = len(_re2.findall(r"\\bclass\\s+\\w+", source))
            parseable = True
        elif filename.lower().endswith((".cbl",".cob")):
            funcs = len(_re2.findall(r"(?mi)^(?:\\d{6}\\s+)?(?!END-)[\\w-]+\\.\\s*$", source))
            classes = 0
            parseable = True
        elif filename.lower().endswith(".java"):
            funcs = len(_re2.findall(r"(?:public|private|protected)\\s+(?:static\\s+)?(?:synchronized\\s+)?[\\w<>\\[\\]]+\\s+\\w+\\s*\\([^)]*\\)\\s*(?:throws\\s+[\\w,\\s]+)?\\s*\\{", source))
            classes = len(_re2.findall(r"\\bclass\\s+\\w+", source))
            parseable = True
        else:
            funcs = len(_re2.findall(r"\\bdef\\s+\\w+\\s*\\(", source)); classes = len(_re2.findall(r"\\bclass\\s+\\w+", source))
            parseable = False
    security_hits = len(_re2.findall(r"(?i)(\\beval\\(|\\bexec\\(|hashlib\\.md5|hashlib\\.sha1|password\\s*=\\s*[\\"\\x27]|verify\\s*=\\s*False|shell\\s*=\\s*True)", source))
    findings = []
    if not parseable and _is_python_file: findings.append("Contains Python 2-only syntax - AST parser has partial visibility here; this is typically auto-fixed during migration, not a blocker")
    if security_hits > 0: findings.append(f"{security_hits} potential security/compliance issue(s) detected")
    if len(lines) > 300: findings.append(f"Large file ({len(lines)} lines) - higher migration effort")
    if not findings: findings.append("No major blockers detected - code appears in reasonable shape")
    health = 100 - (0 if parseable else 30) - min(security_hits*10, 40) - (10 if len(lines) > 300 else 0)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")