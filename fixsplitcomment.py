main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Remove the nested definition (4-space indented, inside migrate_code)
old_nested = '''    def _split_inline_comment(_line):
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
        return _line, ""
'''
results["1_remove_nested"] = content.count(old_nested)
content = content.replace(old_nested, "", 1)

# Add module-level version right before "def migrate_code"
old_before = "def migrate_code(source):"
new_before = '''def _split_inline_comment(_line):
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
    return _line, ""


def migrate_code(source):'''
results["2_add_module_level"] = content.count(old_before)
content = content.replace(old_before, new_before, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXSPLITCOMMENT-DONE")