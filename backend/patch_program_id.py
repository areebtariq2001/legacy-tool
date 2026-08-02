with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if "IDENTIFICATION DIVISION" in upper:
            changes.append("IDENTIFICATION DIVISION removed")
            continue'''

new = '''        if "IDENTIFICATION DIVISION" in upper:
            changes.append("IDENTIFICATION DIVISION removed")
            continue
        prog_id_m = re.match(r"^PROGRAM-ID\\.\\s+([\\w-]+)", line, re.IGNORECASE)
        if prog_id_m:
            out_lines.append("# Program: " + prog_id_m.group(1))
            changes.append("PROGRAM-ID captured as a comment")
            continue'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")