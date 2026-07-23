with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = 1035  # 0-indexed line 1036

if "lambda m:" not in lines[idx]:
    print("SAFETY CHECK FAILED - ABORT")
    print("Actual line:", repr(lines[idx]))
else:
    print("Found dangerous line, replacing:", repr(lines[idx][:80]))
    new_lines = [
        '            buf = ""\n',
        '            in_quote = False\n',
        '            for ch in cond:\n',
        '                if ch == chr(34) or ch == chr(39):\n',
        '                    in_quote = not in_quote\n',
        '                    buf += ch\n',
        '                elif ch == "-" and not in_quote:\n',
        '                    buf += "_"\n',
        '                else:\n',
        '                    buf += ch\n',
        '            cond = buf\n',
    ]
    lines = lines[:idx] + new_lines + lines[idx+1:]
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY - DANGEROUS REGEX REMOVED")