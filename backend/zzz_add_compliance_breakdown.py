with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    return {"exec_health": health, "exec_status": status, "exec_stats": {"lines": len(lines), "functions": funcs, "classes": classes, "security_issues": security_hits}, "exec_findings": findings, "exec_recommendation":'''

new = '''    _compliance_checks = [("AML/KYC reference", r"(?i)(aml|kyc|know.?your.?customer|anti.?money.?launder)"), ("Audit logging", r"(?i)(audit.?log|audit.?trail|write_audit)"), ("Access control", r"(?i)(access.?control|role.?based|permission.?check|authoriz)"), ("Data protection reference", r"(?i)(encrypt|gdpr|data.?protection|pii)")]
    _compliance_present = [name for name, pat in _compliance_checks if _re2.search(pat, source)]
    _compliance_pct = round((len(_compliance_present) / len(_compliance_checks)) * 100)
    _compliance_readiness = {"compliance_readiness_pct": _compliance_pct, "compliance_signals_present": _compliance_present, "compliance_signals_total": len(_compliance_checks), "compliance_note": "Pattern-based signal count, not a compliance certification - a formal review is required."}
    return {"exec_health": health, "exec_status": status, "exec_stats": {"lines": len(lines), "functions": funcs, "classes": classes, "security_issues": security_hits}, "exec_findings": findings, "exec_compliance_readiness": _compliance_readiness, "exec_recommendation":'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")