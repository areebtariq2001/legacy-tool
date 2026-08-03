with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if upper.startswith("WHEN OTHER"):
            if not eval_first_when:
                if_depth = max(0, if_depth - 1)
            out_lines.append(cur_indent() + "else:")
            if_depth += 1
            eval_first_when = False
            changes.append("WHEN OTHER -> else")
            continue'''

new = '''        if upper.startswith("WHEN OTHER"):
            if not eval_first_when:
                if_depth = max(0, if_depth - 1)
            out_lines.append(cur_indent() + "else:")
            if_depth += 1
            eval_first_when = False
            eval_subject = None
            changes.append("WHEN OTHER -> else")
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