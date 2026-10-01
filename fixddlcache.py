main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _create_users_table_if_needed(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, created_at TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS sessions (token TEXT PRIMARY KEY, user_id INTEGER, email TEXT, created_at TEXT, expires_at TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS analyzed_files (id SERIAL PRIMARY KEY, filename TEXT, term_freq_json TEXT, source_excerpt TEXT, created_at TEXT)")'''

new = '''_users_table_initialized = False


def _create_users_table_if_needed(cur):
    global _users_table_initialized
    if _users_table_initialized:
        return
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, created_at TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS sessions (token TEXT PRIMARY KEY, user_id INTEGER, email TEXT, created_at TEXT, expires_at TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS analyzed_files (id SERIAL PRIMARY KEY, filename TEXT, term_freq_json TEXT, source_excerpt TEXT, created_at TEXT)")
    _users_table_initialized = True'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXDDLCACHE-DONE")
else:
    print("FAILED - count was:", count)