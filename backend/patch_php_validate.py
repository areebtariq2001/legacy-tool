with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    changes.append("var -> public")
    return {"migrated_code": migrated, "changes": changes}
# ---------- JAVA ----------'''

new = '''    changes.append("var -> public")
    check = validate_php(migrated)
    return {"migrated_code": migrated, "changes": changes, "validation": check}
# ---------- JAVA ----------'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")