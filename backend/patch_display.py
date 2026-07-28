with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '            content = disp_m.group(1).replace("-", "_")'
new = '            _disp_val = disp_m.group(1)\n            content = _disp_val if (_disp_val.strip().startswith(chr(34)) or _disp_val.strip().startswith(chr(39))) else _disp_val.replace("-", "_")'

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")