with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("migrate_cobol_endpoint_output.txt", "w", encoding="utf-8") as out:
    for i in range(1774, 1786):
        out.write(str(i + 1) + ": " + lines[i])

print("DONE")