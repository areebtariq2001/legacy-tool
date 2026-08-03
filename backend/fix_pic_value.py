with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            var_name = var_m.group(1).replace("-", "_")
            val = var_m.group(2)
            if val:
                out_lines.append(var_name + " = " + val.rstrip("."))
            else:
                out_lines.append(var_name + " = None")'''

new = '''            var_name = var_m.group(1).replace("-", "_")
            val = var_m.group(2)
            if val:
                val_clean = val.rstrip(".").strip()
                val_map = {"SPACES": '""', "SPACE": '""', "ZEROS": "0", "ZERO": "0", "ZEROES": "0", "LOW-VALUES": "None", "LOW-VALUE": "None", "HIGH-VALUES": "None", "HIGH-VALUE": "None"}
                out_lines.append(var_name + " = " + val_map.get(val_clean.upper(), val_clean))
            else:
                out_lines.append(var_name + " = None")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")