with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def assess_dependency_risk(source, filename="file.py"):
    if not filename.lower().endswith(".py"):
        return {"findings": [], "overall_risk": "Not Analyzed", "total_issues": 0, "not_analyzed_reason": "Dependency risk analysis currently only supports Python. This file was not analyzed - do not interpret this as a low-risk result."}
    try:
        tree = ast.parse(source)
        imported = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for a in node.names:
                    imported.add(a.name.split(".")[0])
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    imported.add(node.module.split(".")[0])
    except:
        imported = set()
    findings = []
    seen = set()
    for pattern, category, level, desc, rec in RISK_RULES:
        in_imports = pattern in imported
        in_source = re.search(r'\\b' + re.escape(pattern) + r'\\b', source) is not None
        if (in_imports or in_source) and pattern not in seen:'''

new = '''def assess_dependency_risk(source, filename="file.py"):
    fname_lower = filename.lower()
    if fname_lower.endswith(".cbl") or fname_lower.endswith(".cob"):
        return {"findings": [], "overall_risk": "Not Analyzed", "total_issues": 0, "not_analyzed_reason": "Dependency risk analysis does not apply to COBOL in the same way as library-based languages - COBOL does not have an equivalent package/import ecosystem to scan. This file was not analyzed - do not interpret this as a low-risk result."}
    imported = set()
    if fname_lower.endswith(".py"):
        active_rules = RISK_RULES
        try:
            tree = ast.parse(source)
            for node in ast.walk(tree):
                if isinstance(node, ast.Import):
                    for a in node.names:
                        imported.add(a.name.split(".")[0])
                elif isinstance(node, ast.ImportFrom):
                    if node.module:
                        imported.add(node.module.split(".")[0])
        except:
            imported = set()
    elif fname_lower.endswith(".java"):
        active_rules = JAVA_RISK_RULES
    elif fname_lower.endswith(".php"):
        active_rules = PHP_RISK_RULES
    else:
        active_rules = RISK_RULES
    findings = []
    seen = set()
    for pattern, category, level, desc, rec in active_rules:
        in_imports = pattern in imported
        in_source = re.search(r'\\b' + re.escape(pattern) + r'\\b' if pattern[-1].isalnum() else re.escape(pattern), source) is not None
        if (in_imports or in_source) and pattern not in seen:'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")