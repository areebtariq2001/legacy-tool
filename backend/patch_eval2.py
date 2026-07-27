with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = 1036  # 0-indexed line 1036

if 'if upper.rstrip(' not in lines[idx]:
    print("SAFETY CHECK FAILED")
    print("Actual line:", repr(lines[idx]))
else:
    new_lines = [
        '        if upper.startswith("EVALUATE "):\n',
        '            eval_subject = line[9:].rstrip(".").strip().replace("-", "_")\n',
        '            eval_first_when = True\n',
        '            changes.append("EVALUATE -> if/elif chain")\n',
        '            continue\n',
        '        if upper.startswith("WHEN OTHER"):\n',
        '            if not eval_first_when:\n',
        '                if_depth = max(0, if_depth - 1)\n',
        '            out_lines.append(cur_indent() + "else:")\n',
        '            if_depth += 1\n',
        '            eval_first_when = False\n',
        '            changes.append("WHEN OTHER -> else")\n',
        '            continue\n',
        '        if upper.startswith("WHEN ") and eval_subject is not None:\n',
        '            when_val = line[5:].rstrip(".").strip()\n',
        '            if not eval_first_when:\n',
        '                if_depth = max(0, if_depth - 1)\n',
        '                out_lines.append(cur_indent() + "elif " + eval_subject + " == " + when_val + ":")\n',
        '            else:\n',
        '                out_lines.append(cur_indent() + "if " + eval_subject + " == " + when_val + ":")\n',
        '                eval_first_when = False\n',
        '            if_depth += 1\n',
        '            changes.append("WHEN -> if/elif")\n',
        '            continue\n',
        '        if upper.startswith("END-EVALUATE"):\n',
        '            if_depth = max(0, if_depth - 1)\n',
        '            eval_subject = None\n',
        '            changes.append("END-EVALUATE removed")\n',
        '            continue\n',
    ]
    lines = lines[:idx] + new_lines + lines[idx:]
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED - EVALUATE handling inserted")