with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old_pattern = r'(?m)^\s{0,7}[\w-]+\.\s*$'
new_pattern = r'(?mi)^(?:\d{6}\s+)?(?!END-)[\w-]+\.\s*$'

count = content.count(old_pattern)
print("Occurrences found:", count)

if count > 0:
    content = content.replace(old_pattern, new_pattern)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY -", count, "occurrences fixed")
else:
    print("NO OCCURRENCES FOUND")