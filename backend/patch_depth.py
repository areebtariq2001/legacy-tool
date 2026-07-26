with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

idx = 1056  # 0-indexed line 1057

if "IF -> if (= converted to ==)" not in lines[idx]:
    print("SAFETY CHECK FAILED")
    print("Actual line:", repr(lines[idx]))
else:
    lines.insert(idx, "            if_depth += 1\n")
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED - if_depth increment inserted")