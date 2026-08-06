with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            _m = pattern.findall(ln)
            if _m:
                count += len(_m)
                line_nums.append(str(i+1))'''
new = '''            _m = pattern.findall(ln)
            if _m:
                count += 1
                line_nums.append(str(i+1))'''

count_occ = content.count(old)
print("Total occurrences found across all functions:", count_occ)
content = content.replace(old, new)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED - all occurrences replaced")