with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''    for pattern, msg in cobol_checks:
        if re.search(pattern, source, re.IGNORECASE):
            issues.append(msg)'''
new1 = '''    for pattern, msg in cobol_checks:
        if re.search(pattern, source, re.IGNORECASE):
            issues.append(msg)
    _cobol_paras = re.findall(r"(?mi)^(?:\\d{6}\\s+)?(?!END-)([\\w-]+)\\.\\s*$", source)
    _cobol_paras = list(dict.fromkeys(_cobol_paras))'''

old_return_cobol = '''    return {"issues": issues}'''

count1 = content.count(old1)
print("COBOL loop-insert occurrences:", count1)
if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("COBOL loop-insert PATCHED")

count_ret = content.count(old_return_cobol)
print("Total bare-issues-returns found:", count_ret)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED (step 1)")