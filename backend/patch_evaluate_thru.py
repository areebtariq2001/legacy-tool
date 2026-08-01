with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        if upper.startswith("WHEN ") and eval_subject is not None:
            when_val = line[5:].rstrip(".").strip()
            if not eval_first_when:
                if_depth = max(0, if_depth - 1)
                out_lines.append(cur_indent() + "elif " + eval_subject + " == " + when_val + ":")
            else:
                out_lines.append(cur_indent() + "if " + eval_subject + " == " + when_val + ":")
                eval_first_when = False
            if_depth += 1
            changes.append("WHEN -> if/elif")
            continue'''

new = '''        if upper.startswith("WHEN ") and eval_subject is not None:
            when_val = line[5:].rstrip(".").strip()
            _thru_m = _mre.match(r"^(.+?)\\s+(?:THRU|THROUGH)\\s+(.+)$", when_val, _mre.IGNORECASE)
            if _thru_m:
                when_cond = _thru_m.group(1).strip() + " <= " + eval_subject + " <= " + _thru_m.group(2).strip()
                changes.append("REVIEW NEEDED: WHEN " + when_val + " (THRU/range) converted to a range-check (" + when_cond + ") - verify this matches the intended COBOL range semantics, especially for non-numeric ranges.")
            else:
                when_cond = eval_subject + " == " + when_val
            if not eval_first_when:
                if_depth = max(0, if_depth - 1)
                out_lines.append(cur_indent() + "elif " + when_cond + ":")
            else:
                out_lines.append(cur_indent() + "if " + when_cond + ":")
                eval_first_when = False
            if_depth += 1
            changes.append("WHEN -> if/elif")
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