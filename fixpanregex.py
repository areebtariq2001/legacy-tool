main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = 'r"(?i)(card.?number|cvv|\\\\bpan\\\\b)"'
new = 'r"(?i)(card.?number|cvv|\\bpan\\b)"'

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXPANREGEX-DONE")
else:
    print("FAILED - count was:", count)