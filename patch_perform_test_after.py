with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        perform_m = _mre.match(r"^PERFORM\\s+([\\w-]+)\\s+UNTIL\\s+(.+?)\\.?$", line, _mre.IGNORECASE)
        if perform_m:
            para_name = perform_m.group(1).replace("-", "_").lower()
            cond = perform_m.group(2).replace("-", "_")
            out_lines.append(cur_indent() + "while not (" + cond + "):")
            out_lines.append(cur_indent() + "    " + para_name + "()")
            changes.append("PERFORM UNTIL -> while loop")
            continue'''

new = '''        perform_m = _mre.match(r"^PERFORM\\s+([\\w-]+)\\s+UNTIL\\s+(.+?)\\.?$", line, _mre.IGNORECASE)
        if perform_m:
            para_name = perform_m.group(1).replace("-", "_").lower()
            cond_raw = perform_m.group(2)
            test_after_m = _mre.search(r"\\s+WITH\\s+TEST\\s+AFTER\\s*$", cond_raw, _mre.IGNORECASE)
            if test_after_m:
                cond_raw = cond_raw[:test_after_m.start()]
            cond = cond_raw.replace("-", "_")
            if test_after_m:
                out_lines.append(cur_indent() + "while True:")
                out_lines.append(cur_indent() + "    " + para_name + "()")
                out_lines.append(cur_indent() + "    if (" + cond + "):")
                out_lines.append(cur_indent() + "        break")
                changes.append("REVIEW NEEDED: PERFORM " + perform_m.group(1) + " UNTIL ... WITH TEST AFTER converted to a post-test loop (executes body first, then checks) - verify this matches the intended COBOL semantics.")
            else:
                out_lines.append(cur_indent() + "while not (" + cond + "):")
                out_lines.append(cur_indent() + "    " + para_name + "()")
            changes.append("PERFORM UNTIL -> while loop")
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