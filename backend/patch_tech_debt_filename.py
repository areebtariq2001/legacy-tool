with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        result = calculate_tech_debt(source)
        comp = calculate_complexity(source)'''

new = '''        result = calculate_tech_debt(source, file.filename)
        comp = calculate_complexity(source)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")