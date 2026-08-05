with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("view_1580_1600_output.txt", "w", encoding="utf-8") as out:
    for i in range(1580, 1600):
        out.write(str(i + 1) + ": " + lines[i])

print("DONE")