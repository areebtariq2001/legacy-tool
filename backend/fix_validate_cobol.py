with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def validate_cobol(code):
    lines = [l for l in code.split(chr(10)) if l.strip()]
    issues = []
    has_id_division = "IDENTIFICATION DIVISION" in code.upper()
    has_procedure_division = "PROCEDURE DIVISION" in code.upper()
    if not has_id_division:
        issues.append("No IDENTIFICATION DIVISION found")
    if not has_procedure_division:
        issues.append("No PROCEDURE DIVISION found")
    unterminated = [i + 1 for i, l in enumerate(lines) if l.strip() and not l.strip().endswith(".") and not l.strip().endswith("-") and l.strip().upper() not in ("PROCEDURE DIVISION",) and "DIVISION" not in l.upper() and "SECTION" not in l.upper()]
    if issues:
        return {"valid": False, "validation_message": "Structural issues detected: " + "; ".join(issues) + ". This is a basic structural check, not a full COBOL parser - please review carefully."}
    return {"valid": True, "validation_message": "Basic structural check passed (division presence). This is not a full COBOL parser - please review carefully."}'''

new = '''def validate_cobol(code):
    try:
        ast.parse(code)
        return {"valid": True, "validation_message": "Migrated Python output parses successfully as valid Python syntax. Note: this validates the Python output, not the original COBOL - please review the business logic conversion carefully."}
    except SyntaxError as e:
        return {"valid": False, "validation_message": "Migrated output has a Python syntax error: " + str(e) + ". This migration likely needs manual correction before use."}
    except Exception as e:
        return {"valid": False, "validation_message": "Warning: could not verify migrated output (" + str(e) + "). Please review carefully."}'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")