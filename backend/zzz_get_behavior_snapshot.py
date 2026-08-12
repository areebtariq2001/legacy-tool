with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("zzz_behavior_out.txt", "w", encoding="utf-8") as out:
    for i in range(4365, 4420):
        if i < len(lines):
            out.write(str(i+1) + ": " + lines[i])

print("DONE")