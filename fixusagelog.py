main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''                cur = conn.cursor()
                cur.execute("ALTER TABLE usage_log ADD COLUMN IF NOT EXISTS user_email TEXT")
                cur.execute("ALTER TABLE usage_log ADD COLUMN IF NOT EXISTS ip TEXT")
                cur.execute("INSERT INTO usage_log (action, filename, result_summary, user_email, ip) VALUES (%s, %s, %s, %s, %s)", (action, filename, result_summary, _user_email, _ip))'''

new = '''                cur = conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS usage_log (id SERIAL PRIMARY KEY, action TEXT, filename TEXT, result_summary TEXT, created_at TIMESTAMP DEFAULT NOW())")
                cur.execute("ALTER TABLE usage_log ADD COLUMN IF NOT EXISTS user_email TEXT")
                cur.execute("ALTER TABLE usage_log ADD COLUMN IF NOT EXISTS ip TEXT")
                cur.execute("INSERT INTO usage_log (action, filename, result_summary, user_email, ip) VALUES (%s, %s, %s, %s, %s)", (action, filename, result_summary, _user_email, _ip))'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXUSAGELOG-DONE")
else:
    print("FAILED - count was:", count)