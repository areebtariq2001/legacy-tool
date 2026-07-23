with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        move_m = _mre.match(r"^MOVE\s+(.+?)\s+TO\s+([\w-]+)\.?$", line, _mre.IGNORECASE)
        if move_m:
            src_val = move_m.group(1).replace("-", "_")
            dst_var = move_m.group(2).replace("-", "_")
            out_lines.append((indent if in_procedure else "") + dst_var + " = " + src_val)
            changes.append("MOVE -> assignment")
            continue'''

new = '''        move_m = _mre.match(r"^MOVE\s+(.+?)\s+TO\s+([\w-]+)\.?$", line, _mre.IGNORECASE)
        if move_m:
            src_val = move_m.group(1).strip()
            if not (src_val.startswith(chr(34)) or src_val.startswith(chr(39))):
                src_val = src_val.replace("-", "_")
            dst_var = move_m.group(2).replace("-", "_")
            out_lines.append((indent if in_procedure else "") + dst_var + " = " + src_val)
            changes.append("MOVE -> assignment")
            continue'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY (MOVE string-literal fix)")