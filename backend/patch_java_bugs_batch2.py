with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# Bug 1: PHP double regex pass fix
old1 = '''    for pattern, repl, label in rules:
        if re.search(pattern, migrated):
            migrated = re.sub(pattern, repl, migrated)
            changes.append(label)
    curly_brace_pattern'''
new1 = '''    for pattern, repl, label in rules:
        _new_migrated = re.sub(pattern, repl, migrated)
        if _new_migrated != migrated:
            migrated = _new_migrated
            changes.append(label)
    curly_brace_pattern'''

# Bug 2 + 4 + 6: Java method regex (generics), truncation flag, wildcard imports
old2 = '''    methods = re.findall(r"(?:public|private|protected)\\s+(?:static\\s+)?(?:synchronized\\s+)?[\\w<>\\[\\]]+\\s+(\\w+)\\s*\\([^)]*\\)\\s*(?:throws\\s+[\\w,\\s]+)?\\s*\\{", source)
    imports = re.findall(r"import\\s+([\\w\\.\\*]+);", source)
    methods = [m for m in methods if m not in classes]
    return {"issues": issues, "classes": list(dict.fromkeys(classes)), "methods": list(dict.fromkeys(methods))[:20], "imports": list(dict.fromkeys(imports)), "java_summary": str(len(classes)) + " class(es), " + str(len(methods)) + " method(s), " + str(len(imports)) + " import(s), " + str(len(issues)) + " legacy pattern(s) found"}'''
new2 = '''    methods = re.findall(r"(?:public|private|protected)\\s+(?:static\\s+)?(?:synchronized\\s+)?[\\w<>\\[\\],\\s]+?\\s+(\\w+)\\s*\\([^)]*\\)\\s*(?:throws\\s+[\\w,\\s]+)?\\s*\\{", source)
    imports = re.findall(r"import\\s+([\\w\\.\\*]+);", source)
    methods = [m for m in methods if m not in classes]
    wildcard_imports = [i for i in imports if i.endswith(".*")]
    if wildcard_imports:
        issues.append("Wildcard import(s) found: " + ", ".join(wildcard_imports) + " - use specific imports instead")
    all_methods = list(dict.fromkeys(methods))
    return {"issues": issues, "classes": list(dict.fromkeys(classes)), "methods": all_methods[:20], "total_methods": len(all_methods), "methods_truncated": len(all_methods) > 20, "imports": list(dict.fromkeys(imports)), "java_summary": str(len(classes)) + " class(es), " + str(len(methods)) + " method(s), " + str(len(imports)) + " import(s), " + str(len(issues)) + " legacy pattern(s) found"}'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Bug 1 fix occurrences:", count1)
print("Bug 2/4/6 fix occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Bug 1 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Bug 2/4/6 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")