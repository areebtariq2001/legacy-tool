with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''            _m = pattern.findall(ln)
            if _m:
                count += 1
                line_nums.append(str(i+1))
        if count > 0:
            is_pqc = "PQC Path" in recommendation
            if is_pqc:
                pqc_needed = True
            findings.append({
                "issue": label,
                "severity": severity,
                "occurrences": count,
                "lines": ", ".join(line_nums[:10]),
                "lines_truncated": len(line_nums) > 10,
                "recommendation": recommendation,
                "pqc": is_pqc
            })
    _high_count = sum(1 for f in findings if f["severity"] == "High")
    if _high_count > 0:
        verdict = "CRITICAL: " + str(_high_count) + " broken algorithm(s) found - immediate replacement required"'''

new = '''            _m = pattern.findall(ln)
            if _m:
                count += 1
                line_nums.append(str(i+1))
                if count == 1:
                    _sample_line = ln.strip()[:120]
        if count > 0:
            is_pqc = "PQC Path" in recommendation
            if is_pqc:
                pqc_needed = True
            findings.append({
                "issue": label,
                "severity": severity,
                "occurrences": count,
                "lines": ", ".join(line_nums[:10]),
                "lines_truncated": len(line_nums) > 10,
                "recommendation": recommendation,
                "pqc": is_pqc,
                "evidence": f"First occurrence at line {line_nums[0]}: {_sample_line}"
            })
    _high_count = sum(1 for f in findings if f["severity"] == "High")
    if _high_count > 0:
        verdict = f"CRITICAL: {_high_count} broken algorithm(s) found - immediate replacement required"'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")