with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("line_519_context.txt", "w", encoding="utf-8") as out:
    for i in range(505, 522):
        out.write(str(i + 1) + ": " + lines[i])

print("DONE")