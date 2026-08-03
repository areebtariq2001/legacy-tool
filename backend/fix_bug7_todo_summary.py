with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''        out_lines.append(cur_indent() + "# TODO: manual review - " + line)
    if in_procedure:'''

new1 = '''        out_lines.append(cur_indent() + "# TODO: manual review - " + line)
        _stmt_type_m = re.match(r"^(\\w[\\w-]*)", line)
        if _stmt_type_m:
            _skipped_types.setdefault(_stmt_type_m.group(1).upper(), 0)
            _skipped_types[_stmt_type_m.group(1).upper()] += 1
    if _skipped_types:
        _skip_summary = ", ".join(str(v) + " " + k for k, v in _skipped_types.items())
        changes.append("REVIEW NEEDED: " + str(sum(_skipped_types.values())) + " statement(s) could not be auto-converted and are marked '# TODO' - manual conversion required: " + _skip_summary)
    if in_procedure:'''

old2 = '''    in_working_storage = False
    in_procedure = False
    current_group_01 = None'''
new2 = '''    in_working_storage = False
    in_procedure = False
    current_group_01 = None
    _skipped_types = {}'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Fix 1 occurrences:", count1)
print("Fix 2 occurrences:", count2)

if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Fix 2 (init) PATCHED")
if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Fix 1 (summary) PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")