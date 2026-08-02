with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            cond = cond_raw.replace("-", "_").replace(" = ", " == ")'''

new = '''            cond = _cobol_hyphen_fix(cond_raw)
            cond = re.sub(r"\\bEQUAL\\s+TO\\b|\\bEQUAL\\b", "==", cond, flags=re.IGNORECASE)
            cond = re.sub(r"\\bGREATER\\s+THAN\\s+OR\\s+EQUAL\\s+TO\\b|\\bGREATER\\s+THAN\\s+OR\\s+EQUAL\\b", ">=", cond, flags=re.IGNORECASE)
            cond = re.sub(r"\\bLESS\\s+THAN\\s+OR\\s+EQUAL\\s+TO\\b|\\bLESS\\s+THAN\\s+OR\\s+EQUAL\\b", "<=", cond, flags=re.IGNORECASE)
            cond = re.sub(r"\\bGREATER\\s+THAN\\b", ">", cond, flags=re.IGNORECASE)
            cond = re.sub(r"\\bLESS\\s+THAN\\b", "<", cond, flags=re.IGNORECASE)
            cond = re.sub(r"\\bNOT\\s+EQUAL\\s+TO\\b|\\bNOT\\s+EQUAL\\b", "!=", cond, flags=re.IGNORECASE)
            cond = re.sub(r"\\bZEROS?\\b", "0", cond, flags=re.IGNORECASE)
            cond = re.sub(r"\\bSPACES?\\b", '""', cond, flags=re.IGNORECASE)
            cond = cond.replace(" = ", " == ")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")