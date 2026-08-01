with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def migrate_php(source):
    changes = []
    migrated = source
    rules = [
        (r'\\bmysql_connect\\b', 'mysqli_connect', "mysql_connect -> mysqli_connect"),
        (r'\\bmysql_query\\b', 'mysqli_query', "mysql_query -> mysqli_query"),
        (r'\\bmysql_fetch_array\\b', 'mysqli_fetch_array', "mysql_fetch_array -> mysqli_fetch_array"),
        (r'\\bmysql_fetch_assoc\\b', 'mysqli_fetch_assoc', "mysql_fetch_assoc -> mysqli_fetch_assoc"),
        (r'\\bmysql_fetch_row\\b', 'mysqli_fetch_row', "mysql_fetch_row -> mysqli_fetch_row"),
        (r'\\bmysql_num_rows\\b', 'mysqli_num_rows', "mysql_num_rows -> mysqli_num_rows"),
        (r'\\bmysql_close\\b', 'mysqli_close', "mysql_close -> mysqli_close"),
        (r'\\bmysql_error\\b', 'mysqli_error', "mysql_error -> mysqli_error"),
        (r'\\bmysql_insert_id\\b', 'mysqli_insert_id', "mysql_insert_id -> mysqli_insert_id"),
        (r'\\bmysql_real_escape_string\\b', 'mysqli_real_escape_string', "mysql_real_escape_string -> mysqli_real_escape_string"),
        (r'\\bmysql_select_db\\b', 'mysqli_select_db', "mysql_select_db -> mysqli_select_db"),
        (r'\\bereg_replace\\(', 'preg_replace(', "ereg_replace() -> preg_replace()"),
        (r'\\bereg\\(', 'preg_match(', "ereg() -> preg_match()"),
        (r'\\bsplit\\(', 'explode(', "split() -> explode()"),
        (r'\\bcall_user_method\\b', 'call_user_func', "call_user_method -> call_user_func"),
    ]
    for pattern, repl, label in rules:
        if re.search(pattern, migrated):
            migrated = re.sub(pattern, repl, migrated)
            changes.append(label)'''

new = '''def migrate_php(source):
    changes = []
    migrated = source
    rules = [
        (r'\\bmysql_close\\b', 'mysqli_close', "mysql_close -> mysqli_close"),
        (r'\\bmysql_error\\b', 'mysqli_error', "mysql_error -> mysqli_error"),
        (r'\\bcall_user_method\\b', 'call_user_func', "call_user_method -> call_user_func"),
    ]
    for pattern, repl, label in rules:
        if re.search(pattern, migrated):
            migrated = re.sub(pattern, repl, migrated)
            changes.append(label)
    review_rules = [
        (r'\\bmysql_connect\\b', "mysql_connect() found - migrating to mysqli requires restructuring to pass a connection object as the first argument to every mysqli_* call (mysqli_query($conn, $sql), not just renaming functions)."),
        (r'\\bmysql_query\\b', "mysql_query() found - mysqli_query() requires a connection parameter as the first argument (mysqli_query($conn, $sql)) which cannot be safely auto-inserted."),
        (r'\\bmysql_fetch_array\\b', "mysql_fetch_array() found - migrating to mysqli requires passing the connection object through your query calls first."),
        (r'\\bmysql_fetch_assoc\\b', "mysql_fetch_assoc() found - migrating to mysqli requires passing the connection object through your query calls first."),
        (r'\\bmysql_fetch_row\\b', "mysql_fetch_row() found - migrating to mysqli requires passing the connection object through your query calls first."),
        (r'\\bmysql_num_rows\\b', "mysql_num_rows() found - migrating to mysqli requires passing the connection object through your query calls first."),
        (r'\\bmysql_insert_id\\b', "mysql_insert_id() found - mysqli_insert_id() requires a connection parameter."),
        (r'\\bmysql_real_escape_string\\b', "mysql_real_escape_string() found - mysqli_real_escape_string() requires a connection parameter. Consider using prepared statements instead."),
        (r'\\bmysql_select_db\\b', "mysql_select_db() found - mysqli_select_db() requires a connection parameter."),
        (r'\\beregi\\(', "eregi() found - preg_match() is the replacement, but you must manually wrap your pattern in delimiters (e.g. \\"/pattern/\\") and add the case-insensitive /i flag."),
        (r'\\bereg\\(', "ereg() found - preg_match() is the replacement, but you must manually wrap your pattern in delimiters (e.g. \\"/pattern/\\") - the pattern syntax is not identical."),
        (r'\\beregi_replace\\(', "eregi_replace() found - preg_replace() is the replacement, but you must manually wrap your pattern in delimiters and add the /i flag."),
        (r'\\bereg_replace\\(', "ereg_replace() found - preg_replace() is the replacement, but you must manually wrap your pattern in delimiters (e.g. \\"/pattern/\\") - the pattern syntax is not identical."),
        (r'\\bsplit\\(', "split() found - if the first argument is a regex pattern, use preg_split() (not explode(), which only handles a literal string, not a regex)."),
    ]
    for pattern, msg in review_rules:
        if re.search(pattern, migrated):
            changes.append("REVIEW NEEDED: " + msg)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")