with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '"total_functions": callgraph.get("total_functions", 0),'
new = '"total_functions": callgraph.get("total_functions", 0) or len(analysis.get("functions", [])),'

count = content.count(old)
print("Occurrences found:", count)

if count > 0:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("NOT FOUND")