with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_idx = None
for i, line in enumerate(lines):
    if 'elif ch == "-" and not in_quote:' in line:
        target_idx = i
        break

if target_idx is None:
    print("TARGET NOT FOUND - ABORT")
else:
    print("Found at line", target_idx + 1)
    for j in range(max(0, target_idx-3), min(len(lines), target_idx+6)):
        print(j+1, ":", repr(lines[j]))