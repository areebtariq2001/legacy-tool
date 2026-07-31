with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().startswith("RISK_RULES = ["):
        start = i
        depth = 0
        for j in range(i, len(lines)):
            depth += lines[j].count("[") - lines[j].count("]")
            if depth == 0 and j > i:
                print("RISK_RULES starts at", start + 1, "ends at", j + 1)
                break
        break