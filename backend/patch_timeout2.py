with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_line_num = 132
idx = target_line_num - 1

print("Current line 132:", repr(lines[idx]))

if "timeout=180" in lines[idx]:
    lines[idx] = lines[idx].replace("timeout=180", "timeout=45")
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY")
else:
    print("MISMATCH - line does not contain timeout=180")