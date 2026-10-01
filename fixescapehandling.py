main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _split_inline_comment(_line):
    _in_str = False
    _str_ch = None
    for _ci, _ch in enumerate(_line):
        if _in_str:
            if _ch == _str_ch:
                _in_str = False
        elif _ch in (chr(34), chr(39)):
            _in_str = True
            _str_ch = _ch
        elif _ch == "#" and not _in_str:
            return _line[:_ci], _line[_ci:]
    return _line, ""'''

new = '''def _split_inline_comment(_line):
    _in_str = False
    _str_ch = None
    _escaped = False
    for _ci, _ch in enumerate(_line):
        if _escaped:
            _escaped = False
            continue
        if _in_str and _ch == "\\\\":
            _escaped = True
            continue
        if _in_str:
            if _ch == _str_ch:
                _in_str = False
        elif _ch in (chr(34), chr(39)):
            _in_str = True
            _str_ch = _ch
        elif _ch == "#" and not _in_str:
            return _line[:_ci], _line[_ci:]
    return _line, ""'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXESCAPEHANDLING-DONE")
else:
    print("FAILED - count was:", count)