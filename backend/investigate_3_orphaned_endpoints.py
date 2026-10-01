main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("investigate_3_orphaned_endpoints_result.txt", "w", encoding="utf-8") as out:
    for ep in ['"/cross-language-migrate"', '"/github-issue-fix"', '"/migration-roadmap"']:
        idx = content.find(ep)
        out.write("=== " + ep + " ===\n")
        if idx != -1:
            idx_start = content.rfind("@app.", 0, idx)
            idx_end = content.find("\n@app.", idx+10)
            out.write(content[idx_start:min(idx_end, idx_start+700)] + chr(10) + chr(10))
        else:
            out.write("NOT-FOUND\n\n")
print("INVESTIGATE-3-ORPHANED-ENDPOINTS-DONE")