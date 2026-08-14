with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
fixes = []
old1 = '''return {"error": "Approval save failed safely: " + str(e)}'''
new1 = '''return {"error": f"Approval save failed safely: {e}"}'''
if content.count(old1) == 1:
    content = content.replace(old1, new1, 1)
    fixes.append("Bug-11a fixed")
old2 = '''return {"error": "Could not load approval history: " + str(e)}'''
new2 = '''return {"error": f"Could not load approval history: {e}"}'''
if content.count(old2) == 1:
    content = content.replace(old2, new2, 1)
    fixes.append("Bug-11b fixed")
with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
with open("quick_fixes_log2.txt", "w") as log:
    for f2 in fixes:
        log.write(f2 + chr(10))
print("DONE genuinely")
