with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def validate_php(code):
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
        issues.append("No <?php tag found")'''

new = '''def validate_php(code):
    code_no_strings = re.sub(r'"(?:[^"\\\\\\\\]|\\\\\\\\.)*"', '""', code)
    code_no_strings = re.sub(r"'(?:[^'\\\\\\\\]|\\\\\\\\.)*'", "''", code_no_strings)
    code_no_comments = re.sub(r'//.*', '', code_no_strings)
    code_no_comments = re.sub(r'/\\*.*?\\*/', '', code_no_comments, flags=re.DOTALL)
    open_braces = code_no_comments.count("{")
    close_braces = code_no_comments.count("}")
    open_parens = code_no_comments.count("(")
    close_parens = code_no_comments.count(")")
    has_php_tag = "<?php" in code or "<?" in code
    issues = []
    if open_braces != close_braces:
        issues.append(f"Mismatched braces: {open_braces} open vs {close_braces} close")
    if open_parens != close_parens:
        issues.append(f"Mismatched parentheses: {open_parens} open vs {close_parens} close")
    if not has_php_tag and code.strip():
        issues.append("No <?php tag found")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")