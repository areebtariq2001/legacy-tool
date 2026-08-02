with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''            var_name = compute_m.group(1).replace("-", "_")
            expr = compute_m.group(2).replace("-", "_")'''
new1 = '''            var_name = compute_m.group(1).replace("-", "_")
            expr = _cobol_hyphen_fix(compute_m.group(2))'''

old2 = '''            src_val = add_m.group(1).replace("-", "_")
            dst_var = add_m.group(2).replace("-", "_")'''
new2 = '''            src_val = _cobol_hyphen_fix(add_m.group(1))
            dst_var = add_m.group(2).replace("-", "_")'''

old3 = '''            src_val = sub_m.group(1).replace("-", "_")
            dst_var = sub_m.group(2).replace("-", "_")'''
new3 = '''            src_val = _cobol_hyphen_fix(sub_m.group(1))
            dst_var = sub_m.group(2).replace("-", "_")'''

count1 = content.count(old1)
count2 = content.count(old2)
count3 = content.count(old3)
print("COMPUTE fix occurrences:", count1)
print("ADD fix occurrences:", count2)
print("SUBTRACT fix occurrences:", count3)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("COMPUTE PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("ADD PATCHED")
if count3 == 1:
    content = content.replace(old3, new3, 1)
    print("SUBTRACT PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")