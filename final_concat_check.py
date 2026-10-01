main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    lines = f.readlines()

def scan_func(func_name, lines):
    idx_start = None
    idx_end = None
    for i, l in enumerate(lines):
        if "def " + func_name in l:
            idx_start = i
        if idx_start is not None and i > idx_start and l.startswith("def "):
            idx_end = i
            break
    if idx_start is None:
        return 0
    count = 0
    for i in range(idx_start, idx_end):
        if ' + "' in lines[i] or '" + ' in lines[i]:
            count += 1
    return count

funcs = ["migrate_cobol", "migrate_php", "migrate_java", "analyze_php", "analyze_java", "analyze_cobol"]
with open("final_concat_check_result.txt", "w", encoding="utf-8") as out:
    total = 0
    for f_name in funcs:
        c = scan_func(f_name, lines)
        total += c
        out.write(f_name + ": " + str(c) + chr(10))
    out.write(chr(10) + "GRAND-TOTAL-REMAINING: " + str(total))
print("FINAL-CONCAT-CHECK-DONE")