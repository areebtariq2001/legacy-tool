with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = "def generate_executive_report(source, filename):\n    import re as _re2\n"
new = "def generate_executive_report(source, filename):\n    _re2 = re\n"

count = content.count(old)
print("Step 1 occurrences:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("STEP 1 PATCHED")
else:
    print("STEP 1 FAILED")