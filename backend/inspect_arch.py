with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_line_idx = None
for i in range(1730, 1760):
    if i < len(lines) and 'endswith((".java",".php",".cbl",".cob"))' in lines[i]:
        target_line_idx = i
        break

if target_line_idx is None:
    print("TARGET NOT FOUND IN EXPECTED RANGE - ABORT")
else:
    print("FOUND AT LINE", target_line_idx + 1, ":", repr(lines[target_line_idx]))