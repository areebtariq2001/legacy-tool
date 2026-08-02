with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def extract_java_names(code):
    names = set()
    if not JAVALANG_AVAILABLE:
        return names
    try:
        tree = javalang.parse.parse(code)
        for path, node in tree:
            if hasattr(node, "name") and node.name:
                names.add(node.name)
    except:
        pass
    return names'''

new = '''def extract_java_names(code):
    names = set()
    parsed_ok = False
    if JAVALANG_AVAILABLE:
        try:
            tree = javalang.parse.parse(code)
            for path, node in tree:
                if hasattr(node, "name") and node.name:
                    names.add(node.name)
            parsed_ok = True
        except Exception:
            pass
    if not parsed_ok:
        for _m in re.finditer(r"\\b(?:class|interface|enum)\\s+(\\w+)", code):
            names.add(_m.group(1))
        for _m in re.finditer(r"(?:public|private|protected)\\s+(?:static\\s+)?(?:final\\s+)?[\\w<>\\[\\],\\s]+?\\s+(\\w+)\\s*\\(", code):
            names.add(_m.group(1))
        for _m in re.finditer(r"(?:public|private|protected)\\s+(?:static\\s+)?(?:final\\s+)?[\\w<>\\[\\]]+\\s+(\\w+)\\s*[=;]", code):
            names.add(_m.group(1))
    return names'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")