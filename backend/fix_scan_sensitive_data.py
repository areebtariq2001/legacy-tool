with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def scan_sensitive_data(source):
    findings = []
    source_lines = source.split(chr(10))
    for pattern, label, severity in SENSITIVE_PATTERNS:
        matches = re.findall(pattern, source)
        count = len(matches)
        if count > 0:
            line_nums = [str(i+1) for i, ln in enumerate(source_lines) if re.search(pattern, ln)]
            findings.append({
                "issue": label,
                "severity": severity,
                "occurrences": count,
                "lines": ", ".join(line_nums[:10])
            })
    high = sum(1 for f in findings if f["severity"] == "High")
    medium = sum(1 for f in findings if f["severity"] == "Medium")
    low = sum(1 for f in findings if f["severity"] == "Low")
    if high > 0:
        verdict = "Sensitive data found - review before migration"
    elif medium > 0 or low > 0:
        verdict = "Possible sensitive data - please review"
    else:
        verdict = "No obvious sensitive data detected"'''

new = '''def scan_sensitive_data(source):
    findings = []
    source_lines = source.split(chr(10))
    for pattern, label, severity in SENSITIVE_PATTERNS_COMPILED:
        count = 0
        line_nums = []
        for i, ln in enumerate(source_lines):
            _m = pattern.findall(ln)
            if _m:
                count += len(_m)
                line_nums.append(str(i+1))
        if count > 0:
            findings.append({
                "issue": label,
                "severity": severity,
                "occurrences": count,
                "lines": ", ".join(line_nums[:10]),
                "lines_truncated": len(line_nums) > 10,
                "total_lines_affected": len(line_nums)
            })
    high = sum(1 for f in findings if f["severity"] == "High")
    medium = sum(1 for f in findings if f["severity"] == "Medium")
    low = sum(1 for f in findings if f["severity"] == "Low")
    if high > 3:
        verdict = "CRITICAL: " + str(high) + " high-severity issues found - do not migrate without review"
    elif high > 0:
        verdict = "WARNING: " + str(high) + " high-severity issue(s) found - review before migration"
    elif medium > 0:
        verdict = "CAUTION: " + str(medium) + " medium-severity issue(s) - please review"
    elif low > 0:
        verdict = "Possible sensitive data - please review"
    else:
        verdict = "No obvious sensitive data detected"'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")