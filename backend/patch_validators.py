with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = "def validate_python(code):"
new = '''def validate_php(code):
    open_braces = code.count("{")
    close_braces = code.count("}")
    open_parens = code.count("(")
    close_parens = code.count(")")
    has_php_tag = "<?php" in code or "<?" in code
    issues = []
    if open_braces != close_braces:
        issues.append(f"Mismatched braces: {open_braces} open vs {close_braces} close")
    if open_parens != close_parens:
        issues.append(f"Mismatched parentheses: {open_parens} open vs {close_parens} close")
    if not has_php_tag and code.strip():
        issues.append("No <?php tag found")
    if issues:
        return {"valid": False, "validation_message": "Structural issues detected: " + "; ".join(issues) + ". This is a basic structural check, not a full PHP parser - please review carefully."}
    return {"valid": True, "validation_message": "Basic structural check passed (brace/paren balance). This is not a full PHP parser - please review carefully."}

def validate_cobol(code):
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
    return {"valid": True, "validation_message": "Basic structural check passed (division presence). This is not a full COBOL parser - please review carefully."}

def validate_python(code):'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")