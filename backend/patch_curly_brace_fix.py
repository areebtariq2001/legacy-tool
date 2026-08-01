with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    rules = [
        (r'\\bmysql_close\\b', 'mysqli_close', "mysql_close -> mysqli_close"),
        (r'\\bmysql_error\\b', 'mysqli_error', "mysql_error -> mysqli_error"),
        (r'\\bcall_user_method\\b', 'call_user_func', "call_user_method -> call_user_func"),
    ]'''

new = '''    rules = [
        (r'\\bmysql_close\\b', 'mysqli_close', "mysql_close -> mysqli_close"),
        (r'\\bmysql_error\\b', 'mysqli_error', "mysql_error -> mysqli_error"),
        (r'\\bcall_user_method\\b', 'call_user_func', "call_user_method -> call_user_func"),
    ]
    curly_brace_pattern = r'(\\$\\w+)\\{(\\d+|\\$\\w+)\\}'
    if re.search(curly_brace_pattern, migrated):
        migrated = re.sub(curly_brace_pattern, r'\\1[\\2]', migrated)
        changes.append("curly-brace string/array access {n} -> [n] (curly-brace access removed in PHP 8)")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")