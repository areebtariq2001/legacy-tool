main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''            cur.execute("SELECT filename, decision, reviewer_notes, action_type, timestamp FROM approval_log ORDER BY id DESC")
            rows = cur.fetchall()
            return [{"filename": r[0], "decision": r[1], "reviewer_notes": r[2], "action_type": r[3], "timestamp": r[4]} for r in rows]'''

new = '''            cur.execute("SELECT filename, decision, reviewer_notes, action_type, timestamp, approved_by FROM approval_log ORDER BY id DESC")
            rows = cur.fetchall()
            return [{"filename": r[0], "decision": r[1], "reviewer_notes": r[2], "action_type": r[3], "timestamp": r[4], "approved_by": r[5]} for r in rows]'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXAPPROVALHISTORY-DONE")
else:
    print("FAILED - count was:", count)