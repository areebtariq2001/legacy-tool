with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        ('exec ', "exec statement found - use exec() function"),
        ('<>', "<> operator found - use !="),'''
new = '''        ('<>', "<> operator found - use !="),'''

old2 = '''    if re.search(r'\\bprint\\s+[^(]', source):
        issues.append("print statement found - use print()")'''
new2 = '''    if re.search(r'\\bprint\\s+[^(]', source):
        issues.append("print statement found - use print()")
    if re.search(r'\\bexec\\s+[^(]', source):
        issues.append("exec statement found (Python 2 style, no parentheses) - use exec() function")'''

count1 = content.count(old)
count2 = content.count(old2)
print("Fix 1 occurrences:", count1)
print("Fix 2 occurrences:", count2)

if count1 == 1:
    content = content.replace(old, new, 1)
    print("Fix 1 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Fix 2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")