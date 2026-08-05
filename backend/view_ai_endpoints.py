with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("ai_endpoints_output.txt", "w", encoding="utf-8") as out:
    for i in range(1810, 1850):
        out.write(str(i + 1) + ": " + lines[i])

print("DONE")