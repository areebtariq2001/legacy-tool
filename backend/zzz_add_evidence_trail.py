with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    for i, line in enumerate(lines):
        up = line.upper()
        _matched_this_line = False
        for kw, danger, msg in checks:
            if kw.upper() in up and danger in line:
                _redacted = _sq.sub(r"([\\"\\x27])[^\\"\\x27]*\\{[^}]*\\}[^\\"\\x27]*([\\"\\x27])", r"\\1***\\2", line.strip()[:150])
                issues.append({"line": i+1, "code": _redacted, "issue": msg, "severity": "High"})
                _matched_this_line = True
        if not _matched_this_line and fstring_pattern.search(line):
            _redacted = _sq.sub(r"([\\"\\x27])[^\\"\\x27]*\\{[^}]*\\}[^\\"\\x27]*([\\"\\x27])", r"\\1***\\2", line.strip()[:150])
            issues.append({"line": i+1, "code": _redacted, "issue": "SQL built with f-string interpolation - injection risk", "severity": "High"})
    return {"sqli_safe": len(issues) == 0, "sqli_issues": issues, "sqli_summary": f"{len(issues)} potential SQL injection risk(s) found - review these lines" if issues else "No obvious SQL injection patterns detected in this file", "sqli_disclaimer": "Detects common SQL injection patterns. Pattern-based - always confirm with a security review and use parameterized queries."}'''

new = '''    def _extract_tainted_var(line):
        m = _sq.search(r"[+%]\\s*([a-zA-Z_][\\w\\.\\[\\]\\'\\"]*)", line)
        if m:
            return m.group(1).strip()
        m2 = _sq.search(r"\\{\\s*([a-zA-Z_][\\w\\.\\[\\]]*)\\s*\\}", line)
        if m2:
            return m2.group(1).strip()
        return None
    for i, line in enumerate(lines):
        up = line.upper()
        _matched_this_line = False
        for kw, danger, msg in checks:
            if kw.upper() in up and danger in line:
                _redacted = _sq.sub(r"([\\"\\x27])[^\\"\\x27]*\\{[^}]*\\}[^\\"\\x27]*([\\"\\x27])", r"\\1***\\2", line.strip()[:150])
                _tainted = _extract_tainted_var(line)
                issues.append({"line": i+1, "code": _redacted, "issue": msg, "severity": "High", "likely_source_variable": _tainted, "evidence": (f"Untrusted value flows from variable '{_tainted}' directly into the SQL string on this line." if _tainted else "Untrusted value flows directly into the SQL string on this line.")})
                _matched_this_line = True
        if not _matched_this_line and fstring_pattern.search(line):
            _redacted = _sq.sub(r"([\\"\\x27])[^\\"\\x27]*\\{[^}]*\\}[^\\"\\x27]*([\\"\\x27])", r"\\1***\\2", line.strip()[:150])
            _tainted = _extract_tainted_var(line)
            issues.append({"line": i+1, "code": _redacted, "issue": "SQL built with f-string interpolation - injection risk", "severity": "High", "likely_source_variable": _tainted, "evidence": (f"Untrusted value flows from variable '{_tainted}' directly into the SQL string on this line." if _tainted else "Untrusted value flows directly into the SQL string on this line.")})
    return {"sqli_safe": len(issues) == 0, "sqli_issues": issues, "sqli_summary": f"{len(issues)} potential SQL injection risk(s) found - review these lines" if issues else "No obvious SQL injection patterns detected in this file", "sqli_disclaimer": "Detects common SQL injection patterns. Pattern-based - always confirm with a security review and use parameterized queries. 'likely_source_variable' is a best-effort guess from the matched line, not a verified data-flow trace across the file."}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")