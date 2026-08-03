with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        out_lines.append("if __name__ == " + chr(39) + "__main__" + chr(39) + ":")'''
new = '''        out_lines.append("if __name__ == '__main__':")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")