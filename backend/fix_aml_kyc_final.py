with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''write_audit_log("extract-aml-kyc", file.filename, "findings=" + str(result.get("total_findings", 0)))'''
new1 = '''write_audit_log("extract-aml-kyc", file.filename, f"findings={result.get('total_findings', 0)}")'''

old2 = '''    if findings:
        verdict = "AML/KYC compliance logic detected - review with compliance team"
    else:
        verdict = "No obvious AML/KYC patterns detected"
    return {
        "findings": findings,
        "total_findings": len(findings),
        "verdict": verdict,
        "has_compliance_logic": len(findings) > 0,
        "disclaimer": "Keyword-based detector for AML/KYC-related logic. This is a discovery aid to help locate compliance-critical code. A compliance officer must verify all findings - this does not certify regulatory compliance."
    }'''

new2 = '''    aml_count = sum(1 for f in findings if f["category"] == "AML")
    kyc_count = sum(1 for f in findings if f["category"] == "KYC")
    if aml_count > 0 and kyc_count > 0:
        verdict = "CRITICAL: Both AML (" + str(aml_count) + ") and KYC (" + str(kyc_count) + ") logic detected - full compliance review required"
    elif aml_count > 0:
        verdict = "WARNING: AML logic detected (" + str(aml_count) + " pattern(s)) - compliance review required"
    elif kyc_count > 0:
        verdict = "WARNING: KYC logic detected (" + str(kyc_count) + " pattern(s)) - compliance review required"
    else:
        verdict = "No obvious AML/KYC patterns detected"
    return {
        "findings": findings,
        "total_findings": len(findings),
        "aml_findings": aml_count,
        "kyc_findings": kyc_count,
        "verdict": verdict,
        "has_compliance_keywords": len(findings) > 0,
        "compliance_review_required": len(findings) > 0,
        "disclaimer": "Keyword-based detector for AML/KYC-related logic. This is a discovery aid to help locate compliance-critical code. A compliance officer must verify all findings - this does not certify regulatory compliance."
    }'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Fix-1 (f-string) occurrences:", count1)
print("Fix-2 (verdict+counts) occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Fix-1 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Fix-2 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")