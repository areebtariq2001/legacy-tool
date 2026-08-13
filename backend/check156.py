with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("check_line156.txt", "w", encoding="utf-8") as out:
    for i in range(145, 165):
        out.write(str(i+1) + ": " + repr(lines[i]) + chr(10))
print("DONE genuinely")
