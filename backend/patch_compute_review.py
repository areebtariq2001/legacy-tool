with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        compute_m = _mre.match(r"^COMPUTE\\s+([\\w-]+)\\s*=\\s*(.+?)\\.?$", line, _mre.IGNORECASE)
        if compute_m:
            var_name = compute_m.group(1).replace("-", "_")
            expr = compute_m.group(2).replace("-", "_")
            out_lines.append(cur_indent() + var_name + " = " + expr)
            changes.append("COMPUTE -> assignment")
            continue'''

new = '''        compute_m = _mre.match(r"^COMPUTE\\s+([\\w-]+)\\s*=\\s*(.+?)\\.?$", line, _mre.IGNORECASE)
        if compute_m:
            var_name = compute_m.group(1).replace("-", "_")
            expr = compute_m.group(2).replace("-", "_")
            out_lines.append(cur_indent() + var_name + " = " + expr)
            changes.append("COMPUTE -> assignment")
            if "/" in expr or "*" in expr:
                changes.append("REVIEW NEEDED: COMPUTE " + var_name + " = " + expr + " - COBOL fixed-point decimal arithmetic (based on the field's PIC clause) truncates by default unless ROUNDED is specified, which differs from Python's native arithmetic. Verify this calculation produces the intended result, especially for financial/numeric logic.")
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