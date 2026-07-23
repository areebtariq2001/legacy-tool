with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if 'buf = ""' in line and i > 1030 and i < 1045:
        start_idx = i
    if start_idx is not None and 'cond = buf' in line:
        end_idx = i
        break

if start_idx is None or end_idx is None:
    print("BLOCK NOT FOUND - ABORT")
    print("start_idx:", start_idx, "end_idx:", end_idx)
else:
    print("Replacing lines", start_idx+1, "to", end_idx+1)
    new_lines = [
        '            words = cond.split(" ")\n',
        '            fixed_words = []\n',
        '            for w in words:\n',
        '                if w and w[0] not in (chr(34), chr(39)) and "-" in w and any(c.isalnum() for c in w):\n',
        '                    fixed_words.append(w.replace("-", "_"))\n',
        '                else:\n',
        '                    fixed_words.append(w)\n',
        '            cond = " ".join(fixed_words)\n',
    ]
    lines = lines[:start_idx] + new_lines + lines[end_idx+1:]
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY - word-based hyphen fix")