with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith("def calculate_complexity("):
        start = i
        for j in range(i, min(i + 30, len(lines))):
            print(j + 1, ":", lines[j], end="")
        break