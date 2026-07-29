with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# Step 1: Remove the WRONGLY placed patch
wrong = '''    check = validate_cobol(migrated)
    return {"migrated_code": migrated, "changes": changes, "why_explanations": get_why_explanations(source), "dependencies": check_dependencies(source), "validation": check}'''
correct_original = '''    return {"migrated_code": migrated, "changes": changes, "why_explanations": get_why_explanations(source), "dependencies": check_dependencies(source)}'''

count_wrong = content.count(wrong)
print("Wrong placements found:", count_wrong)

if count_wrong >= 1:
    content = content.replace(wrong, correct_original)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("REVERTED")
else:
    print("Nothing to revert")