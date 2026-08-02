with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        (r'PIC\\s+9', "PIC 9 numeric fields - convert to int/float"),
        (r'PIC\\s+X', "PIC X string fields - convert to str"),'''

new = '''        (r'\\bPIC\\s+9', "PIC 9 numeric fields - convert to int/float"),
        (r'\\bPIC\\s+X', "PIC X string fields - convert to str"),'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")