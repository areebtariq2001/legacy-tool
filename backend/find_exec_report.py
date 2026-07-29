with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if line.strip().startswith("def generate_executive_report"):
        print("FOUND AT LINE:", i + 1)
        for j in range(i, min(i + 20, len(lines))):
            print(j + 1, ":", lines[j], end="")
        break