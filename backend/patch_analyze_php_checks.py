with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        (r'\\beach\\(', "each() found - use foreach loop"),
        (r'\\bcall_user_method\\b', "call_user_method() found - use call_user_func()"),
        (r'\\bget_magic_quotes_gpc\\b', "get_magic_quotes_gpc() found - removed in PHP 7"),
    ]'''

new = '''        (r'\\beach\\(', "each() found - use foreach loop"),
        (r'\\bcall_user_method\\b', "call_user_method() found - use call_user_func()"),
        (r'\\bget_magic_quotes_gpc\\b', "get_magic_quotes_gpc() found - removed in PHP 7"),
        (r'\\bpreg_replace\\s*\\([^)]*[\\x22\\x27][^\\x22\\x27]*e[\\x22\\x27]', "preg_replace() with /e modifier found - the /e modifier was removed in PHP 7, use preg_replace_callback() instead"),
        (r'\\$HTTP_(GET|POST|COOKIE|SERVER|ENV|SESSION)_VARS\\b', "$HTTP_*_VARS superglobal found - removed in PHP 5.4+, use $_GET/$_POST/etc. instead"),
        (r'\\bset_magic_quotes_runtime\\b', "set_magic_quotes_runtime() found - removed in PHP 7"),
        (r'\\bini_set\\s*\\(\\s*[\\x22\\x27]safe_mode', "safe_mode ini setting found - removed in PHP 7, has no effect"),
        (r'\\bereg_replace\\(', "ereg_replace() found - use preg_replace() (pattern needs delimiters added)"),
        (r'\\bsql_regcase\\b', "sql_regcase() found - removed in PHP 7"),
    ]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")