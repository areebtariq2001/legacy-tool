with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        move_m = re.match(r"^MOVE\\s+(.+?)\\s+TO\\s+([\\w-]+)\\.?$", line, re.IGNORECASE)
        if move_m:
            src_val = move_m.group(1).strip()
            is_literal = src_val.startswith(chr(34)) or src_val.startswith(chr(39)) or re.match(r"^-?\\d+(\\.\\d+)?$", src_val)
            if not is_literal:
                src_val_clean = src_val.replace("-", "_")
            else:
                src_val_clean = src_val
            dst_var = move_m.group(2).replace("-", "_")
            out_lines.append(cur_indent() + dst_var + " = " + src_val_clean)
            changes.append("MOVE -> assignment")'''

new = '''        move_m = re.match(r"^MOVE\\s+(.+?)\\s+TO\\s+([\\w\\s-]+)\\.?$", line, re.IGNORECASE)
        if move_m:
            src_val = move_m.group(1).strip()
            is_literal = src_val.startswith(chr(34)) or src_val.startswith(chr(39)) or re.match(r"^-?\\d+(\\.\\d+)?$", src_val)
            if not is_literal:
                src_val_clean = src_val.replace("-", "_")
            else:
                src_val_clean = src_val
            dst_vars = [d.replace("-", "_") for d in move_m.group(2).strip().split()]
            for dst_var in dst_vars:
                out_lines.append(cur_indent() + dst_var + " = " + src_val_clean)
            changes.append("MOVE -> assignment" + (" (" + str(len(dst_vars)) + " destinations)" if len(dst_vars) > 1 else ""))'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")