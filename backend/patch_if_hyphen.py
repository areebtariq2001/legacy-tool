with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            cond = _mre.sub(r"(?<![=<>!])=(?!=)", "==", cond)
            out_lines.append((indent if in_procedure else "") + "if " + cond + ":")
            changes.append("IF -> if (with = converted to ==)")
            continue'''

new = '''        if upper.startswith("IF "):
            cond = line[3:].rstrip(".")
            cond = _mre.sub(r"(?<![=<>!])=(?!=)", "==", cond)
            cond = _mre.sub(r"[\x22\x27][^\x22\x27]*[\x22\x27]|[A-Za-z][\w-]*", lambda m: m.group(0) if (m.group(0)[0] in chr(34)+chr(39)) else m.group(0).replace("-", "_"), cond)
            out_lines.append((indent if in_procedure else "") + "if " + cond + ":")
            changes.append("IF -> if (with = converted to == and variable hyphens fixed)")
            continue'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY (IF variable hyphen fix)")