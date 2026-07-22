with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

marker = '        if upper.startswith("IF "):'

if marker not in content:
    print("MARKER NOT FOUND - ABORT")
else:
    addition = '''        compute_m = _mre.match(r"^COMPUTE\\s+([\\w-]+)\\s*=\\s*(.+?)\\.?$", line, _mre.IGNORECASE)
        if compute_m:
            var_name = compute_m.group(1).replace("-", "_")
            expr = compute_m.group(2).replace("-", "_")
            out_lines.append((indent if in_procedure else "") + var_name + " = " + expr)
            changes.append("COMPUTE -> assignment")
            continue
        add_m = _mre.match(r"^ADD\\s+(.+?)\\s+TO\\s+([\\w-]+)\\.?$", line, _mre.IGNORECASE)
        if add_m:
            src_val = add_m.group(1).replace("-", "_")
            dst_var = add_m.group(2).replace("-", "_")
            out_lines.append((indent if in_procedure else "") + dst_var + " += " + src_val)
            changes.append("ADD -> +=")
            continue
        sub_m = _mre.match(r"^SUBTRACT\\s+(.+?)\\s+FROM\\s+([\\w-]+)\\.?$", line, _mre.IGNORECASE)
        if sub_m:
            src_val = sub_m.group(1).replace("-", "_")
            dst_var = sub_m.group(2).replace("-", "_")
            out_lines.append((indent if in_procedure else "") + dst_var + " -= " + src_val)
            changes.append("SUBTRACT -> -=")
            continue
        perform_m = _mre.match(r"^PERFORM\\s+([\\w-]+)\\s+UNTIL\\s+(.+?)\\.?$", line, _mre.IGNORECASE)
        if perform_m:
            para_name = perform_m.group(1).replace("-", "_").lower()
            cond = perform_m.group(2).replace("-", "_")
            out_lines.append((indent if in_procedure else "") + "while not (" + cond + "):")
            out_lines.append((indent if in_procedure else "") + "    " + para_name + "()")
            changes.append("PERFORM UNTIL -> while loop")
            continue
'''
    content = content.replace(marker, addition + marker)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")