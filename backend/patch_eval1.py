with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '    if_depth = 0\n    def cur_indent():\n        return "    " * (1 + if_depth) if in_procedure else "    " * if_depth'
new = old + '\n    eval_subject = None\n    eval_first_when = False'

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("STEP1 PATCHED")
else:
    print("STEP1 FAILED")