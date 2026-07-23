with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            out_lines.append((indent if in_procedure else "") + "if " + cond + ":")
            changes.append("IF -> if")
            continue'''

new = '''        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            cond = _mre.sub(r"(?<![=<>!])=(?!=)", "==", cond)
            out_lines.append((indent if in_procedure else "") + "if " + cond + ":")
            changes.append("IF -> if (with = converted to ==)")
            continue'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY (IF condition fix)")