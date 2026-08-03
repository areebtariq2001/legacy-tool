with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''    in_working_storage = False
    in_procedure = False'''
new1 = '''    in_working_storage = False
    in_procedure = False
    current_group_01 = None'''

old2 = '''        var_m = re.match(r"^\\d+\\s+([\\w-]+)\\s+PIC\\s+\\S+(?:\\s+VALUE\\s+(.+?))?\\.?$", line, re.IGNORECASE)
        if var_m and in_working_storage:
            var_name = var_m.group(1).replace("-", "_")
            val = var_m.group(2)
            if val:
                val_clean = val.rstrip(".").strip()
                val_map = {"SPACES": '""', "SPACE": '""', "ZEROS": "0", "ZERO": "0", "ZEROES": "0", "LOW-VALUES": "None", "LOW-VALUE": "None", "HIGH-VALUES": "None", "HIGH-VALUE": "None"}
                out_lines.append(var_name + " = " + val_map.get(val_clean.upper(), val_clean))
            else:
                out_lines.append(var_name + " = None")
            changes.append("Variable " + var_m.group(1) + " declared")
            continue'''
new2 = '''        var_m = re.match(r"^(\\d+)\\s+([\\w-]+)\\s+PIC\\s+\\S+(?:\\s+VALUE\\s+(.+?))?\\.?$", line, re.IGNORECASE)
        if var_m and in_working_storage:
            level_num = var_m.group(1)
            raw_name = var_m.group(2).replace("-", "_")
            if level_num == "01":
                current_group_01 = raw_name
                var_name = raw_name
            elif current_group_01:
                var_name = current_group_01 + "_" + raw_name
            else:
                var_name = raw_name
            val = var_m.group(3)
            if val:
                val_clean = val.rstrip(".").strip()
                val_map = {"SPACES": '""', "SPACE": '""', "ZEROS": "0", "ZERO": "0", "ZEROES": "0", "LOW-VALUES": "None", "LOW-VALUE": "None", "HIGH-VALUES": "None", "HIGH-VALUE": "None"}
                out_lines.append(var_name + " = " + val_map.get(val_clean.upper(), val_clean))
            else:
                out_lines.append(var_name + " = None")
            changes.append("Variable " + var_m.group(2) + " declared" + (" (level " + level_num + ", nested under " + current_group_01 + ")" if level_num != "01" and current_group_01 else ""))
            continue
        group_m = re.match(r"^(\\d+)\\s+([\\w-]+)\\.?$", line, re.IGNORECASE)
        if group_m and in_working_storage and group_m.group(1) == "01":
            current_group_01 = group_m.group(2).replace("-", "_")
            out_lines.append("# Group: " + current_group_01)
            changes.append("Group-level record " + group_m.group(2) + " noted")
            continue'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Fix 1 occurrences:", count1)
print("Fix 2 occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Fix 1 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Fix 2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")