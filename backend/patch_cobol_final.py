with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_line_num = 1144  # 1-indexed
idx = target_line_num - 1

if lines[idx].strip() == 'return {"migrated_code": migrated, "changes": changes}':
    indent = lines[idx][:len(lines[idx]) - len(lines[idx].lstrip())]
    new_lines = [
        indent + "check = validate_cobol(migrated)\n",
        indent + 'return {"migrated_code": migrated, "changes": changes, "validation": check}\n'
    ]
    lines[idx:idx+1] = new_lines
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY at line", target_line_num)
else:
    print("MISMATCH - line content was:", repr(lines[idx]))
    print("ABORTING to be safe")