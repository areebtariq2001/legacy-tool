main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Add a new C-style (//) comment-splitting function at module level, right after
# the existing Python-style (#) one, for use by Java/PHP migration where // is a
# comment marker (and # is not used at all, unlike Python where // is integer division)
old1 = '''def migrate_code(source):'''
new1 = '''def _split_inline_comment_cstyle(_line):
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
        elif _ch == "/" and _ci + 1 < len(_line) and _line[_ci + 1] == "/" and not _in_str:
            return _line[:_ci], _line[_ci:]
    return _line, ""


def migrate_code(source):'''
results["1_add_cstyle_function"] = content.count(old1)
content = content.replace(old1, new1, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXJAVACOMMENT-DONE")