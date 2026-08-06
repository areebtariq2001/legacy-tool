with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    new_lines = []
    for line in migrated.split('\\n'):
        m = re.match(r'^(\\s*)print\\s+(?!\\()(.+?)\\s*$', line)
        if m:
            new_lines.append(f'{m.group(1)}print({m.group(2)})')
            if "print statement -> print()" not in changes:
                changes.append("print statement -> print()")
        else:
            new_lines.append(line)
    migrated = '\\n'.join(new_lines)'''

new = '''    new_lines = []
    for line in migrated.split('\\n'):
        m = re.match(r'^(\\s*)print\\s+(?!\\()(.+)$', line)
        if m:
            indent = m.group(1)
            rest = m.group(2)
            _cm = re.search(r'^((?:[^\\x27\\x22#]|\\x27[^\\x27]*\\x27|\\x22[^\\x22]*\\x22)*?)\\s*(#.*)$', rest)
            if _cm and _cm.group(1).strip():
                code_part = _cm.group(1).rstrip()
                comment_part = _cm.group(2)
                new_lines.append(f'{indent}print({code_part})  {comment_part}')
            else:
                new_lines.append(f'{indent}print({rest.rstrip()})')
            if "print statement -> print()" not in changes:
                changes.append("print statement -> print()")
        else:
            new_lines.append(line)
    migrated = '\\n'.join(new_lines)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")