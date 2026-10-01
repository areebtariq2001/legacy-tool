main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''            _code_part, _comment_part = _split_inline_comment(_mline)
            _new_code_part = re.sub(pattern, repl, _code_part)
            _new_line = _new_code_part + _comment_part'''

new = '''            _code_part, _comment_part = _split_inline_comment(_mline)
            _str_literals = []
            def _mask_str(m):
                _str_literals.append(m.group(0))
                return "\\x00STRLIT" + str(len(_str_literals) - 1) + "\\x00"
            _masked_code_part = re.sub(r'"(?:[^"\\\\]|\\\\.)*"|\\'(?:[^\\'\\\\]|\\\\.)*\\'', _mask_str, _code_part)
            _new_masked_code_part = re.sub(pattern, repl, _masked_code_part)
            _new_code_part = re.sub(r'\\x00STRLIT(\\d+)\\x00', lambda m: _str_literals[int(m.group(1))], _new_masked_code_part)
            _new_line = _new_code_part + _comment_part'''

remaining = content.count(old)
print("Remaining occurrences (before):", remaining)
content = content.replace(old, new)
final = content.count(old)
print("After replace, remaining:", final)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)
print("FIXSTRINGLITERAL2-DONE")