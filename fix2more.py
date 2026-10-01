main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: correct the scan-repo disclaimer text to reflect actual 4-language support
old1 = 'Only Python files are currently supported - Java/PHP/COBOL repo-scanning is not yet available. For full/large repos, a paid server and deeper analysis are planned.'
new1 = 'Python, Java, PHP, and COBOL files are scanned. For full/large repos, a paid server and deeper analysis are planned.'
results["1_disclaimer_fix"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: previous_content should return the actual previous doc content, not its hash
old2 = '''            cur.execute("SELECT version, doc_hash FROM docs_registry WHERE filename = %s ORDER BY version DESC LIMIT 1", (filename,))
            row = cur.fetchone()
            if row and row[1] == doc_hash:
                return {"saved": True, "is_new_version": False, "version": row[0], "message": "Documentation unchanged since last version - no new version created."}
            new_version = (row[0] + 1) if row else 1
            timestamp = datetime.now().isoformat()
            cur.execute("INSERT INTO docs_registry (filename, doc_content, doc_hash, version, created_at) VALUES (%s, %s, %s, %s, %s)", (filename, doc_content, doc_hash, new_version, timestamp))
            conn.commit()
            return {"saved": True, "is_new_version": True, "version": new_version, "created_at": timestamp, "previous_content": (row[1] if row else None)}'''
new2 = '''            cur.execute("SELECT version, doc_hash, doc_content FROM docs_registry WHERE filename = %s ORDER BY version DESC LIMIT 1", (filename,))
            row = cur.fetchone()
            if row and row[1] == doc_hash:
                return {"saved": True, "is_new_version": False, "version": row[0], "message": "Documentation unchanged since last version - no new version created."}
            new_version = (row[0] + 1) if row else 1
            timestamp = datetime.now().isoformat()
            cur.execute("INSERT INTO docs_registry (filename, doc_content, doc_hash, version, created_at) VALUES (%s, %s, %s, %s, %s)", (filename, doc_content, doc_hash, new_version, timestamp))
            conn.commit()
            return {"saved": True, "is_new_version": True, "version": new_version, "created_at": timestamp, "previous_content": (row[2] if row else None)}'''
results["2_previous_content_fix"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIX2MORE-DONE")