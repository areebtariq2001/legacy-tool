with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

matches = [(i+1, l.rstrip()) for i, l in enumerate(lines) if "analyze_call_graph" in l]

with open("zzz_refs_output.txt", "w", encoding="utf-8") as f:
    for lineno, text in matches:
        f.write(str(lineno) + ": " + text + "\n")

print("DONE - total refs:", len(matches))