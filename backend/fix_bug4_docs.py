with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def validate_cobol(code):
    try:
        ast.parse(code)
        return {"valid": True, "validation_message": "Migrated Python output parses successfully as valid Python syntax. Note: this validates the Python output, not the original COBOL - please review the business logic conversion carefully."}'''

new = '''def validate_cobol(code):
    # Note: despite the name (kept for naming-consistency with validate_java/validate_php),
    # this validates the MIGRATED PYTHON OUTPUT, not the original COBOL source.
    # COBOL syntax validation would require a dedicated COBOL parser, which is not used here.
    try:
        ast.parse(code)
        return {"valid": True, "validation_message": "Migrated Python output parses successfully as valid Python syntax. Note: this validates the Python output, not the original COBOL - please review the business logic conversion carefully."}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")