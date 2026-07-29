with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if line.strip().startswith("async def explain_endpoint"):
        print("FOUND AT LINE:", i + 1)
        for j in range(i, min(i + 15, len(lines))):
            print(j + 1, ":", lines[j], end="")
        break