with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def check_ai_native_readiness(source, filename="file.py"):'''
new = '''def check_ai_native_readiness(source, filename=""):'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")