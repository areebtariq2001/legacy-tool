with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("3_new_locations_output.txt", "w", encoding="utf-8") as out:
    for target in [1008, 1963, 2824]:
        idx = target - 1
        out.write("=== AROUND LINE " + str(target) + " ===\n")
        for j in range(max(0, idx - 15), min(idx + 3, len(lines))):
            if "def " in lines[j] or j >= idx - 3:
                out.write(str(j + 1) + ": " + lines[j])
        out.write("\n")

print("DONE")