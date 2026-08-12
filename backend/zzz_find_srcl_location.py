with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("zzz_srcl_loc_out.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        if "src_l = source.lower()" in line:
            out.write("Line " + str(i+1) + ": " + line)
            for j in range(max(0,i-5), i):
                out.write("  context " + str(j+1) + ": " + lines[j])

print("DONE")