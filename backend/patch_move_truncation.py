with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        move_m = _mre.match(r"^MOVE\\s+(.+?)\\s+TO\\s+([\\w-]+)\\.?$", line, _mre.IGNORECASE)
        if move_m:
            src_val = move_m.group(1).strip()
            if not (src_val.startswith(chr(34)) or src_val.startswith(chr(39))):
                src_val = src_val.replace("-", "_")
            dst_var = move_m.group(2).replace("-", "_")
            out_lines.append(cur_indent() + dst_var + " = " + src_val)
            changes.append("MOVE -> assignment")
            continue'''

new = '''        move_m = _mre.match(r"^MOVE\\s+(.+?)\\s+TO\\s+([\\w-]+)\\.?$", line, _mre.IGNORECASE)
        if move_m:
            src_val = move_m.group(1).strip()
            is_literal = src_val.startswith(chr(34)) or src_val.startswith(chr(39)) or _mre.match(r"^-?\\d+(\\.\\d+)?$", src_val)
            if not is_literal:
                src_val_clean = src_val.replace("-", "_")
            else:
                src_val_clean = src_val
            dst_var = move_m.group(2).replace("-", "_")
            out_lines.append(cur_indent() + dst_var + " = " + src_val_clean)
            changes.append("MOVE -> assignment")
            if not is_literal:
                changes.append("REVIEW NEEDED: MOVE " + move_m.group(1).strip() + " TO " + move_m.group(2) + " - COBOL MOVE truncates or pads based on the destination field's PIC clause size, which this migration does not replicate. Verify field lengths match, especially for financial/fixed-width data.")
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