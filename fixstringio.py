main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = "    (r'\\bStringIO\\b', \"StringIO\", 10),"
new = "    (r'(?:^|\\n)\\s*(?:import\\s+StringIO\\b|from\\s+StringIO\\s+import)', \"StringIO (standalone module)\", 10),"

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXSTRINGIO-DONE")
else:
    print("FAILED - count was:", count)