with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def detect_language(filename):
    ext = filename.split('.')[-1].lower()
    return {"py": "python", "java": "java", "php": "php", "cbl": "cobol"}.get(ext, "python")'''

new = '''def detect_language(filename):
    if not filename or filename.startswith('.') or '.' not in filename:
        return "unknown"
    ext = filename.rsplit('.', 1)[-1].lower()
    return {
        "py": "python",
        "java": "java",
        "php": "php", "php3": "php", "php5": "php", "phtml": "php",
        "cbl": "cobol", "cob": "cobol", "cobol": "cobol",
    }.get(ext, "unknown")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")