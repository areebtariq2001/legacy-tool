with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            if test_after_m:
                cond_raw = cond_raw[:test_after_m.start()]
            cond = cond_raw.replace("-", "_")'''

new = '''            if test_after_m:
                cond_raw = cond_raw[:test_after_m.start()]
            cond = cond_raw.replace("-", "_").replace(" = ", " == ")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")