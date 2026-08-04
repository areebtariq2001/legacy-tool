with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("full_3_functions.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "def " in line and 985 <= i+1 <= 1015:
            out.write(str(i+1) + ": " + line)

print("DONE")