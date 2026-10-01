main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''def _create_users_table_if_needed(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, created_at TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS sessions (token TEXT PRIMARY KEY, user_id INTEGER, email TEXT, created_at TEXT, expires_at TEXT)")'''

new = '''def _create_users_table_if_needed(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL, created_at TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS sessions (token TEXT PRIMARY KEY, user_id INTEGER, email TEXT, created_at TEXT, expires_at TEXT)")
    cur.execute("CREATE TABLE IF NOT EXISTS analyzed_files (id SERIAL PRIMARY KEY, filename TEXT, term_freq_json TEXT, source_excerpt TEXT, created_at TEXT)")


def _extract_term_frequencies(source, max_terms=100):
    _words = re.findall(r"[a-zA-Z_][a-zA-Z0-9_]{2,}", source.lower())
    _STOPWORDS = {"the", "and", "for", "not", "this", "that", "with", "from", "true", "false", "none", "self", "def", "return", "import", "class"}
    _freq = {}
    for _w in _words:
        if _w in _STOPWORDS:
            continue
        _freq[_w] = _freq.get(_w, 0) + 1
    _top = dict(sorted(_freq.items(), key=lambda kv: -kv[1])[:max_terms])
    return _top


def _cosine_similarity_termfreq(freq_a, freq_b):
    _common = set(freq_a.keys()) & set(freq_b.keys())
    if not _common:
        return 0.0
    _dot = sum(freq_a[w] * freq_b[w] for w in _common)
    _mag_a = sum(v * v for v in freq_a.values()) ** 0.5
    _mag_b = sum(v * v for v in freq_b.values()) ** 0.5
    if _mag_a == 0 or _mag_b == 0:
        return 0.0
    return _dot / (_mag_a * _mag_b)


def store_analyzed_file(filename, source):
    conn = _get_db_connection()
    if not conn:
        return False
    cur = None
    try:
        cur = conn.cursor()
        _create_users_table_if_needed(cur)
        _term_freq = _extract_term_frequencies(source)
        _excerpt = source[:500]
        cur.execute(
            "INSERT INTO analyzed_files (filename, term_freq_json, source_excerpt, created_at) VALUES (%s, %s, %s, %s)",
            (filename, json.dumps(_term_freq), _excerpt, datetime.now().isoformat())
        )
        conn.commit()
        cur.execute("DELETE FROM analyzed_files WHERE id NOT IN (SELECT id FROM analyzed_files ORDER BY id DESC LIMIT 500)")
        conn.commit()
        return True
    except Exception:
        return False
    finally:
        if cur:
            cur.close()
        conn.close()


def find_similar_files(source, limit=3, exclude_filename=None):
    conn = _get_db_connection()
    if not conn:
        return []
    cur = None
    try:
        cur = conn.cursor()
        _query_freq = _extract_term_frequencies(source)
        cur.execute("SELECT filename, term_freq_json, source_excerpt FROM analyzed_files ORDER BY id DESC LIMIT 500")
        rows = cur.fetchall()
        _scored = []
        for _fname, _tf_json, _excerpt in rows:
            if exclude_filename and _fname == exclude_filename:
                continue
            try:
                _tf = json.loads(_tf_json)
            except Exception:
                continue
            _score = _cosine_similarity_termfreq(_query_freq, _tf)
            if _score > 0.1:
                _scored.append({"filename": _fname, "similarity": round(_score, 3), "excerpt": _excerpt})
        _scored.sort(key=lambda x: -x["similarity"])
        return _scored[:limit]
    except Exception:
        return []
    finally:
        if cur:
            cur.close()
        conn.close()'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("SIMILARITY-STAGE1-IMPLEMENTED")
else:
    print("FAILED - count was:", count)