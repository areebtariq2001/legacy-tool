with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
with open("broken_lines_context.txt", "w", encoding="utf-8") as out:
    for i in range(5360, 5372):
        out.write(str(i+1) + ": " + repr(lines[i]) + chr(10))
print("BROKEN-LINES-COMPLETED")