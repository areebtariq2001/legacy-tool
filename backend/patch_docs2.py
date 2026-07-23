with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    doc["living_doc_summary"] = "Documentation version " + str(save_result.get("version", 1)) + " of " + str(len(history)) + " total - " + ("new version saved" if save_result.get("is_new_version") else "unchanged since last save")'''

new = '''    if not save_result.get("saved"):
        doc["living_doc_summary"] = "Documentation generated, but versioned storage is not available right now (database unreachable) - this version was not saved."
    else:
        doc["living_doc_summary"] = "Documentation version " + str(save_result.get("version", 1)) + " of " + str(len(history)) + " total - " + ("new version saved" if save_result.get("is_new_version") else "unchanged since last save")'''

if old not in content:
    print("OLD STRING NOT FOUND - ABORT")
else:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")