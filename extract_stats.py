with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "def load_stats(" in line or "def save_stats(" in line or "def track_usage(" in line or 'STATS_FILE' in line:
        output_lines.append(str(i + 1) + ": " + lines[i])

with open("stats_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE")