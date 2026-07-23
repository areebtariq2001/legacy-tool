with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

marker = "def _get_db_connection():"

if marker not in content:
    print("MARKER NOT FOUND - ABORT")
else:
    new_func = '''def save_living_documentation(filename, doc_content, doc_hash):
    import datetime as _dt
    conn = _get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS docs_registry (id SERIAL PRIMARY KEY, filename TEXT, doc_content TEXT, doc_hash TEXT, version INTEGER, created_at TEXT)")
            cur.execute("SELECT version, doc_hash FROM docs_registry WHERE filename = %s ORDER BY version DESC LIMIT 1", (filename,))
            row = cur.fetchone()
            if row and row[1] == doc_hash:
                cur.close()
                conn.close()
                return {"saved": True, "is_new_version": False, "version": row[0], "message": "Documentation unchanged since last version - no new version created."}
            new_version = (row[0] + 1) if row else 1
            timestamp = _dt.datetime.now().isoformat()
            cur.execute("INSERT INTO docs_registry (filename, doc_content, doc_hash, version, created_at) VALUES (%s, %s, %s, %s, %s)", (filename, doc_content, doc_hash, new_version, timestamp))
            conn.commit()
            cur.close()
            conn.close()
            return {"saved": True, "is_new_version": True, "version": new_version, "created_at": timestamp, "previous_content": row and None}
        except Exception as e:
            return {"saved": False, "error": str(e)}
    return {"saved": False, "error": "Database not available"}

def get_living_documentation_history(filename):
    conn = _get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT version, doc_content, created_at FROM docs_registry WHERE filename = %s ORDER BY version DESC", (filename,))
            rows = cur.fetchall()
            cur.close()
            conn.close()
            return [{"version": r[0], "doc_content": r[1], "created_at": r[2]} for r in rows]
        except Exception:
            return []
    return []

def generate_living_documentation(source, filename):
    import hashlib as _hl
    doc = generate_documentation(source, filename)
    doc_text = doc.get("ai_documentation", "")
    doc_hash = _hl.md5(doc_text.encode("utf-8", errors="ignore")).hexdigest()
    save_result = save_living_documentation(filename, doc_text, doc_hash)
    history = get_living_documentation_history(filename)
    doc["living_doc_version"] = save_result.get("version", 1)
    doc["living_doc_is_new_version"] = save_result.get("is_new_version", False)
    doc["living_doc_total_versions"] = len(history)
    doc["living_doc_history"] = [{"version": h["version"], "created_at": h["created_at"]} for h in history]
    doc["living_doc_summary"] = "Documentation version " + str(save_result.get("version", 1)) + " of " + str(len(history)) + " total - " + ("new version saved" if save_result.get("is_new_version") else "unchanged since last save")
    doc["living_doc_disclaimer"] = "Documentation is versioned and stored persistently. A new version is only saved when the generated content actually changes, avoiding duplicate entries on repeated runs."
    return doc

'''
    content = content.replace(marker, new_func + marker)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")