with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = 1033

if 'if upper.startswith("IF "):' not in lines[idx]:
    print("SAFETY CHECK FAILED")
    print("Actual line:", repr(lines[idx]))
else:
    new_lines = [
        '        if upper.rstrip(".") == "ELSE":\n',
        '            if_depth = max(0, if_depth - 1)\n',
        '            out_lines.append(cur_indent() + "else:")\n',
        '            if_depth += 1\n',
        '            changes.append("ELSE -> else")\n',
        '            continue\n',
        '        if upper.startswith("END-IF"):\n',
        '            if_depth = max(0, if_depth - 1)\n',
        '            changes.append("END-IF removed (Python uses indentation)")\n',
        '            continue\n',
        '        if upper.startswith("IF "):\n',
    ]
    lines = lines[:idx] + new_lines + lines[idx+1:]
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED - inserted ELSE/END-IF handling before IF block")