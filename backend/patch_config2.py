with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_idx = None
for i, line in enumerate(lines):
    if "hardcoded_patterns = [" in line and "password|passwd|pwd" in line:
        target_idx = i
        break

if target_idx is None:
    print("TARGET LINE NOT FOUND - ABORT")
else:
    cobol_addition = '''    if filename.lower().endswith((".cbl", ".cob")):
        hardcoded_patterns += [(r"(?i)[\w-]*(password|passwd|pwd)[\w-]*\s+PIC\s+X.*VALUE\s+[\"\x27][^\"\x27]{2,}[\"\x27]", "Hardcoded credential (password, COBOL VALUE clause)", "CRITICAL: Never hardcode passwords - move to a secrets manager or environment variable immediately"), (r"(?i)[\w-]*(username|user_name|db.?user)[\w-]*\s+PIC\s+X.*VALUE\s+[\"\x27][^\"\x27]{2,}[\"\x27]", "Hardcoded credential (username, COBOL VALUE clause)", "Move to environment variable (e.g. DB_USER)"), (r"(?i)[\w-]*(host|hostname|server)[\w-]*\s+PIC\s+X.*VALUE\s+[\"\x27][^\"\x27]{2,}[\"\x27]", "Hardcoded host/server address (COBOL VALUE clause)", "Move to environment variable (e.g. DB_HOST) or a config file loaded at startup")]
'''
    lines.insert(target_idx + 1, cobol_addition)
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY at line", target_idx + 1)