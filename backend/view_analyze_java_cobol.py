with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("analyze_java_cobol_output.txt", "w", encoding="utf-8") as out:
    for i in range(1740, 1780):
        out.write(str(i + 1) + ": " + lines[i])

print("DONE")