with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "lambda m:" in line:
        print("FOUND AT LINE", i+1, ":", repr(line[:100]))