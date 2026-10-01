main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

tests = [
    "categories - showing first",
    "mainframe-specific construct",
    'str(len(top_categories))',
    "top_categories)) + ",
]

with open("diag_result.txt", "w", encoding="utf-8") as out:
    for t in tests:
        out.write(repr(t) + " -> count: " + str(content.count(t)) + chr(10))
print("DIAG-DONE")