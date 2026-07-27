with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'upper.rstrip(' in line and 'ELSE' in line:
        print("FOUND AT LINE", i+1, "(0-indexed:", i, ")")
        print(repr(line))