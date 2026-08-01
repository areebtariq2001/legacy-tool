with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''        changes.append("var -> public")'''
new1 = '''        changes.append("var -> public (PHP officially treats 'var' as a synonym for 'public' - this is not a guess, it is the documented PHP behavior)")'''

old2 = '''"java_summary": str(len(classes)) + " class(es), " + str(len(methods)) + " method(s), " + str(len(imports)) + " import(s), " + str(len(issues)) + " legacy pattern(s) found"}'''
new2 = '''"java_summary": f"{len(classes)} class(es), {len(methods)} method(s), {len(imports)} import(s), {len(issues)} legacy pattern(s) found"}'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Bug 7 occurrences:", count1)
print("Bug 8 occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Bug 7 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Bug 8 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")