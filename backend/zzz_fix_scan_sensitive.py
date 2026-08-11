with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            _m = pattern.findall(ln)
            if _m:
                count += 1
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

new = '''            _m = pattern.findall(ln)
            if _m:
                count += 1
                line_nums.append(str(i+1))
                if count == 1:
                    _sample_line = ln.strip()[:120]
        if count > 0:
            findings.append({
                "issue": label,
                "severity": severity,
                "occurrences": count,
                "lines": ", ".join(line_nums[:10]),
                "lines_truncated": len(line_nums) > 10,
                "total_lines_affected": len(line_nums),
                "evidence": f"First occurrence at line {line_nums[0]}: {_sample_line}"
            })
    high = sum(1 for f in findings if f["severity"] == "High")
    medium = sum(1 for f in findings if f["severity"] == "Medium")
    low = sum(1 for f in findings if f["severity"] == "Low")
    if high > 3:
        verdict = f"CRITICAL: {high} high-severity issues found - do not migrate without review"
    elif high > 0:
        verdict = f"WARNING: {high} high-severity issue(s) found - review before migration"
    elif medium > 0:
        verdict = f"CAUTION: {medium} medium-severity issue(s) - please review"
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