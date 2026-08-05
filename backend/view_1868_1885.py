with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("view_1868_1885_output.txt", "w", encoding="utf-8") as out:
    for i in range(1866, 1885):
        out.write(str(i + 1) + ": " + repr(lines[i]) + "\n")

print("DONE")