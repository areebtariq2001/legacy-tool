main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: mask string literals before regex substitution in the main rules loop,
# so patterns don't match text that appears inside a Java string literal
old1 = '''            _code_part, _comment_part = _split_inline_comment(_mline)
            _new_code_part = re.sub(pattern, repl, _code_part)
            _new_line = _new_code_part + _comment_part'''
new1 = '''            _code_part, _comment_part = _split_inline_comment(_mline)
            _str_literals = []
            def _mask_str(m):
                _str_literals.append(m.group(0))
                return "\\x00STRLIT" + str(len(_str_literals) - 1) + "\\x00"
            _masked_code_part = re.sub(r'"(?:[^"\\\\]|\\\\.)*"', _mask_str, _code_part)
            _new_masked_code_part = re.sub(pattern, repl, _masked_code_part)
            _new_code_part = re.sub(r'\\x00STRLIT(\\d+)\\x00', lambda m: _str_literals[int(m.group(1))], _new_masked_code_part)
            _new_line = _new_code_part + _comment_part'''
results["1_mask_string_literals"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: strip // and /* */ comments before running review_rules checks,
# so a comment mentioning e.g. "StringBuffer" doesn't false-positive
old2 = '''    for pattern, msg in review_rules:
        if re.search(pattern, migrated):
            changes.append(f"REVIEW NEEDED: {msg}")
    check = validate_java(migrated)'''
new2 = '''    _migrated_no_comments = re.sub(r'/\\*.*?\\*/', '', migrated, flags=re.DOTALL)
    _migrated_no_comments = chr(10).join(_split_inline_comment(_l)[0] for _l in _migrated_no_comments.split(chr(10)))
    for pattern, msg in review_rules:
        if re.search(pattern, _migrated_no_comments):
            changes.append(f"REVIEW NEEDED: {msg}")
    check = validate_java(migrated)'''
results["2_review_rules_strip_comments"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXJAVASTRINGLITERAL-DONE")