main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Add a PHP-specific comment-splitting function (PHP supports both # and // as line comments)
old1 = '''def migrate_java(source):'''
new1 = '''def _split_inline_comment_php(_line):
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
        elif _ch == "/" and _ci + 1 < len(_line) and _line[_ci + 1] == "/" and not _in_str:
            return _line[:_ci], _line[_ci:]
    return _line, ""


def migrate_java(source):'''
results["1_add_php_function"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Update migrate_php's main rules loop and review_rules-equivalent to use the PHP-specific splitter
idx_start = content.find("def migrate_php")
idx_end = content.find("\ndef ", idx_start + 20)
php_body = content[idx_start:idx_end]

old2 = "_code_part, _comment_part = _split_inline_comment(_mline)"
results["2_php_main_loop_count"] = php_body.count(old2)
new_php_body = php_body.replace(old2, "_code_part, _comment_part = _split_inline_comment_php(_mline)")

old3 = '''    for pattern, msg in review_rules:
        if re.search(pattern, migrated):
            changes.append(f"REVIEW NEEDED: {msg}")'''
new3 = '''    _migrated_no_comments_php = re.sub(r'/\\*.*?\\*/', '', migrated, flags=re.DOTALL)
    _migrated_no_comments_php = chr(10).join(_split_inline_comment_php(_l)[0] for _l in _migrated_no_comments_php.split(chr(10)))
    for pattern, msg in review_rules:
        if re.search(pattern, _migrated_no_comments_php):
            changes.append(f"REVIEW NEEDED: {msg}")'''
results["3_php_review_rules_count"] = new_php_body.count(old3)
new_php_body = new_php_body.replace(old3, new3, 1)

content = content[:idx_start] + new_php_body + content[idx_end:]

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXPHPCOMMENT-DONE")