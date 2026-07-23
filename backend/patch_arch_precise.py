with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = 1749  # 0-indexed line 1750

if 'endswith((".java",".php",".cbl",".cob"))' not in lines[idx]:
    print("SAFETY CHECK FAILED - line does not match expected content - ABORT")
    print("Actual line:", repr(lines[idx]))
else:
    new_lines = [
        '        if filename.lower().endswith((".cbl", ".cob")):\n',
        '            funcs = _re.findall(r"(?m)^\\s{0,7}([\\w-]+)\\.\\s*$", source)\n',
        '            classes = []\n',
        '            imports = []\n',
        '        elif filename.lower().endswith((".java",".php")):\n',
    ]
    lines = lines[:idx] + new_lines + lines[idx+1:]
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY")