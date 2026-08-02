with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def analyze_cobol(source):
    issues = []
    cobol_checks = [
        ('PERFORM', "PERFORM found - convert to functions/loops"),
        ('GOTO', "GOTO found - use structured programming"),
        ('GO TO', "GO TO found - use structured programming"),
        ('PIC 9', "PIC 9 numeric fields - convert to int/float"),
        ('PIC X', "PIC X string fields - convert to str"),
        ('MOVE', "MOVE statement - use Python assignment"),
        ('COMPUTE', "COMPUTE found - use Python arithmetic"),
        ('ACCEPT', "ACCEPT found - use input()"),
        ('STOP RUN', "STOP RUN found - use return/exit"),
        ('WORKING-STORAGE', "WORKING-STORAGE section - convert to variables"),
        ('PERFORM UNTIL', "PERFORM UNTIL - convert to while loop"),
    ]
    for pattern, msg in cobol_checks:
        if pattern in source:
            issues.append(msg)'''

new = '''def analyze_cobol(source):
    issues = []
    cobol_checks = [
        (r'PERFORM\\s+UNTIL', "PERFORM UNTIL found - convert to while loop"),
        (r'PERFORM\\s+VARYING', "PERFORM VARYING found - convert to for loop"),
        (r'PERFORM\\s+\\w[\\w-]*\\s+THRU', "PERFORM THRU found - calls a range of paragraphs, convert to sequential function calls"),
        (r'PERFORM\\s+\\w[\\w-]*(?!\\s+(?:UNTIL|VARYING|THRU))', "PERFORM (paragraph call) found - convert to a function call"),
        (r'GOTO|GO\\s+TO', "GO TO found - use structured programming"),
        (r'PIC\\s+9', "PIC 9 numeric fields - convert to int/float"),
        (r'PIC\\s+X', "PIC X string fields - convert to str"),
        (r'MOVE', "MOVE statement - use Python assignment"),
        (r'COMPUTE', "COMPUTE found - use Python arithmetic"),
        (r'ACCEPT', "ACCEPT found - use input()"),
        (r'STOP\\s+RUN', "STOP RUN found - use return/exit"),
        (r'WORKING-STORAGE', "WORKING-STORAGE section - convert to variables"),
        (r'REDEFINES', "REDEFINES found - memory overlay reinterpretation, needs manual review (no direct Python equivalent)"),
        (r'OCCURS', "OCCURS found - array/table definition, convert to a Python list"),
        (r'\\bCOPY\\b', "COPY statement found - copybook dependency, resolve/inline the copybook before migration"),
        (r'FILE\\s+SECTION', "FILE SECTION found - file I/O definitions, need manual conversion to Python file handling"),
        (r'\\bFD\\b', "FD (file descriptor) found - needs manual conversion to Python file handling"),
        (r'\\bCALL\\s', "CALL found - calls an external program, verify the target program exists and is migrated"),
        (r'EXEC\\s+SQL', "EXEC SQL found - embedded SQL, migrate to a Python DB driver (e.g. using parameterized queries)"),
        (r'DISPLAY', "DISPLAY found - output statement, convert to print()"),
    ]
    for pattern, msg in cobol_checks:
        if re.search(r'\\b' + pattern.replace(chr(92)+"b","") if False else pattern, source, re.IGNORECASE):
            issues.append(msg)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")