with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

start = None
for i, line in enumerate(lines):
    if line.strip().startswith("def migrate_cobol("):
        start = i
        break

if start is not None:
    depth_zero_seen_def = False
    for i in range(start + 1, min(start + 400, len(lines))):
        stripped = lines[i].strip()
        if stripped.startswith("def ") and not lines[i].startswith("    "):
            print(f"NEXT FUNCTION STARTS AT LINE {i+1}: {stripped}")
            break
        if "return {" in lines[i] or (stripped.startswith("return") and "{" in lines[i]):
            print(f"LINE {i+1}: {lines[i].rstrip()}")
else:
    print("migrate_cobol not found")