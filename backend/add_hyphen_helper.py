with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = "def migrate_cobol(source):"
new = '''def _cobol_hyphen_fix(s):
    return re.sub(r"(?<=[A-Za-z0-9])-(?=[A-Za-z])", "_", s)

def migrate_cobol(source):'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")