with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    return {"migrated_code": migrated, "changes": changes, "why_explanations": get_why_explanations(source), "dependencies": check_dependencies(source)}'''

new = '''    check = validate_cobol(migrated)
    return {"migrated_code": migrated, "changes": changes, "why_explanations": get_why_explanations(source), "dependencies": check_dependencies(source), "validation": check}'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")