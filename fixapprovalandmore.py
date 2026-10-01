main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1a: save_approval_decision signature - add approved_by param
old1a = 'def save_approval_decision(filename, decision, reviewer_notes, action_type):'
new1a = 'def save_approval_decision(filename, decision, reviewer_notes, action_type, approved_by=None):'
results["1a_signature"] = content.count(old1a)
content = content.replace(old1a, new1a, 1)

# Fix 1b: CREATE TABLE + ALTER TABLE + INSERT to include approved_by
old1b = '''cur.execute("CREATE TABLE IF NOT EXISTS approval_log (id SERIAL PRIMARY KEY, filename TEXT, decision TEXT, reviewer_notes TEXT, action_type TEXT, timestamp TEXT)")
            cur.execute("INSERT INTO approval_log (filename, decision, reviewer_notes, action_type, timestamp) VALUES (%s, %s, %s, %s, %s)", (filename, decision, reviewer_notes, action_type, entry["timestamp"]))'''
new1b = '''cur.execute("CREATE TABLE IF NOT EXISTS approval_log (id SERIAL PRIMARY KEY, filename TEXT, decision TEXT, reviewer_notes TEXT, action_type TEXT, timestamp TEXT)")
            cur.execute("ALTER TABLE approval_log ADD COLUMN IF NOT EXISTS approved_by TEXT")
            cur.execute("INSERT INTO approval_log (filename, decision, reviewer_notes, action_type, timestamp, approved_by) VALUES (%s, %s, %s, %s, %s, %s)", (filename, decision, reviewer_notes, action_type, entry["timestamp"], approved_by or "anonymous"))'''
results["1b_table_insert"] = content.count(old1b)
content = content.replace(old1b, new1b, 1)

# Fix 1c: caller endpoint passes real authenticated email
old1c = '''        result = save_approval_decision(filename, decision, reviewer_notes, action_type)
        result["approved_by"] = _user_email'''
new1c = '''        result = save_approval_decision(filename, decision, reviewer_notes, action_type, approved_by=_user_email)
        result["approved_by"] = _user_email'''
results["1c_caller"] = content.count(old1c)
content = content.replace(old1c, new1c, 1)

# Fix 2: find_similar_files - add transparency about global (cross-user) search scope
old2 = '''        _scored.sort(key=lambda x: -x["similarity"])
        return _scored[:limit]
    except Exception:
        return []
    finally:
        if cur:
            cur.close()
        conn.close()


def find_similar_files(source, limit=3, exclude_filename=None):'''
# this pattern won't match uniquely since find_similar_files appears once; targeting its own return instead
results["2_skip"] = 0

old2b = '''            if _score > 0.1:
                _scored.append({"filename": _fname, "similarity": round(_score, 3), "excerpt": _excerpt})
        _scored.sort(key=lambda x: -x["similarity"])
        return _scored[:limit]'''
new2b = '''            if _score > 0.1:
                _scored.append({"filename": _fname, "similarity": round(_score, 3), "excerpt": _excerpt, "note": "Matched against all files previously analyzed by any user of this tool, not just your own uploads."})
        _scored.sort(key=lambda x: -x["similarity"])
        return _scored[:limit]'''
results["2_disclaimer"] = content.count(old2b)
content = content.replace(old2b, new2b, 1)

# Fix 3: soften "execution-ready" overclaim in deep_verify_python
old3 = '"verify_message": f"Compilation failed: syntax error on line {e.lineno}. Code is not execution-ready."'
new3 = '"verify_message": f"Syntax error on line {e.lineno} - code will not run. This checks syntax validity only, not runtime correctness (undefined names, missing imports, or logic errors are not detected)."'
results["3_soften_claim"] = content.count(old3)
content = content.replace(old3, new3, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXBATCH-DONE")