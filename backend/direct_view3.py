main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

for i in range(3799, 3811):
    print(str(i+1) + ": " + lines[i], end="")