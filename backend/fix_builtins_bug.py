with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''_PY_BUILTINS = set(dir(__builtins__)) if isinstance(__builtins__, type(__builtins__)) else set(vars(__builtins__).keys())
_PY_BUILTINS |= {"True", "False", "None", "self", "cls"}'''

new = '''_PY_BUILTINS = set(__builtins__.keys()) if isinstance(__builtins__, dict) else set(dir(__builtins__))
_PY_BUILTINS |= {"True", "False", "None", "self", "cls"}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")