with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            if stripped.startswith(("if ", "for ", "while ", "elif ")):'''

new = '''            if stripped.lower().startswith(("if ", "for ", "while ", "elif ")):'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")