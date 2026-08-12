with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

line_nums = [99, 542, 1136, 2206, 3741, 4387]

with open("zzz_context_except_out.txt", "w", encoding="utf-8") as out:
    for ln in line_nums:
        out.write("=== Around line " + str(ln) + " ===\n")
        start = max(0, ln-6)
        end = min(len(lines), ln+2)
        for i in range(start, end):
            out.write(str(i+1) + ": " + lines[i])
        out.write("\n")

print("DONE")