with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        disp_m = re.match(r"^DISPLAY\\s+(.+?)\\.?$", line, re.IGNORECASE)
        if disp_m:
            _disp_val = disp_m.group(1)
            content = _disp_val if (_disp_val.strip().startswith(chr(34)) or _disp_val.strip().startswith(chr(39))) else _disp_val.replace("-", "_")
            out_lines.append(cur_indent() + "print(" + content + ")")
            changes.append("DISPLAY -> print()")
            continue'''

new = '''        disp_m = re.match(r"^DISPLAY\\s+(.+?)\\.?$", line, re.IGNORECASE)
        if disp_m:
            _disp_val = disp_m.group(1)
            _tokens = re.findall(r'"[^"]*"|\\x27[^\\x27]*\\x27|\\S+', _disp_val)
            _parts = []
            for _t in _tokens:
                if _t.startswith('"') or _t.startswith(chr(39)):
                    _parts.append(_t)
                else:
                    _parts.append(_cobol_hyphen_fix(_t))
            disp_content = " + ".join(_parts) if len(_parts) > 1 else (_parts[0] if _parts else '""')
            out_lines.append(cur_indent() + "print(" + disp_content + ")")
            changes.append("DISPLAY -> print()")
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