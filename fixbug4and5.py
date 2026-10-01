main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix Bug 4: track_usage missing CREATE TABLE
old1 = '''def track_usage(action, filename):
    conn = _get_db_connection()
    if conn:
        cur = None
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO usage_log (action, filename, result_summary) VALUES (%s, %s, %s)", (action, filename, "tracked"))
            conn.commit()
        except Exception:
            pass'''
new1 = '''def track_usage(action, filename):
    conn = _get_db_connection()
    if conn:
        cur = None
        try:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS usage_log (id SERIAL PRIMARY KEY, action TEXT, filename TEXT, result_summary TEXT, created_at TIMESTAMP DEFAULT NOW())")
            cur.execute("INSERT INTO usage_log (action, filename, result_summary) VALUES (%s, %s, %s)", (action, filename, "tracked"))
            conn.commit()
        except Exception:
            pass'''
results["1_track_usage_create_table"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix Bug 5: /download missing try/except around migration calls
old2 = '''    if lang == "java":
        result = migrate_java(source)
    elif lang == "php":
        result = migrate_php(source)
    elif lang == "cobol":
        result = migrate_cobol(source, file.filename)
    else:
        result = migrate_code(source)
    migrated = result.get("migrated_code", "")'''
new2 = '''    try:
        if lang == "java":
            result = migrate_java(source)
        elif lang == "php":
            result = migrate_php(source)
        elif lang == "cobol":
            result = migrate_cobol(source, file.filename)
        else:
            result = migrate_code(source)
    except Exception as e:
        return Response(content=f"Migration failed safely: {e}".encode('utf-8'), media_type='text/plain', status_code=500)
    migrated = result.get("migrated_code", "")'''
results["2_download_tryexcept"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXBUG4AND5-DONE")