with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

start_marker = "def analyze_regulation_impact(source, filename):"
positions = []
start = 0
while True:
    idx = content.find(start_marker, start)
    if idx == -1:
        break
    positions.append(idx)
    start = idx + 1

print("Genuinely-found-copies:", len(positions))

if len(positions) >= 2:
    first_start = positions[0]
    last_start = positions[-1]
    
    genuine_single_copy_end = positions[1]
    genuine_single_copy = content[first_start:genuine_single_copy_end]
    
    end_marker = "def calculate_change_risk_radar(source, filename):"
    after_all_duplicates = content.find(end_marker, last_start)
    
    before = content[:first_start]
    after = content[after_all_duplicates:]
    content = before + genuine_single_copy + after
    
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    
    new_count = content.count(start_marker)
    print("DEDUP-COMPLETE. Genuinely-new-count:", new_count)
else:
    print("Genuinely-no-duplicates-found-or-only-1-copy")