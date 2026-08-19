with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

anchor = "def analyze_regulation_impact(source, filename):"
positions = []
start = 0
while True:
    idx = content.find(anchor, start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + 1

with open("investigate_result.txt", "w", encoding="utf-8") as out:
    out.write("Total-genuinely-found: " + str(len(positions)) + chr(10))
    for p in positions:
        out.write("=== position " + str(p) + " ===" + chr(10))
        out.write(content[max(0,p-50):p+100])
        out.write(chr(10) + chr(10))
print("INVESTIGATE-COMPLETED")