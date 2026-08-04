with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("func_before_1008.txt", "w", encoding="utf-8") as out:
    for i in range(1007, 950, -1):
        if lines[i].strip().startswith("def "):
            out.write("FOUND: line " + str(i+1) + ": " + lines[i])
            break

print("DONE")