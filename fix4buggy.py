main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# Fix 1: LIBOR/SOFR
old1 = '    findings = findings[:30]\n    return {"checked": True, "findings": findings, "total_findings": len(findings), "summary": str(len(findings)) + " LIBOR reference(s) found'
new1 = '    findings_full = findings\n    findings = findings_full[:30]\n    return {"checked": True, "findings": findings, "total_findings": len(findings_full), "findings_shown": len(findings), "findings_truncated": len(findings_full) > 30, "summary": str(len(findings_full)) + " LIBOR reference(s) found'
results["1_libor"] = content.count(old1)
content = content.replace(old1, new1, 1)

# Fix 2: SWIFT MT / ISO 20022
old2 = '    findings = findings[:30]\n    return {"checked": True, "findings": findings, "total_findings": len(findings), "summary": str(len(findings)) + " legacy SWIFT MT reference(s) found'
new2 = '    findings_full = findings\n    findings = findings_full[:30]\n    return {"checked": True, "findings": findings, "total_findings": len(findings_full), "findings_shown": len(findings), "findings_truncated": len(findings_full) > 30, "summary": str(len(findings_full)) + " legacy SWIFT MT reference(s) found'
results["2_swift"] = content.count(old2)
content = content.replace(old2, new2, 1)

# Fix 3: Riba flag
old3 = '    findings = findings[:30]\n    return {"checked": True, "findings": findings, "total_findings": len(findings), "summary": str(len(findings)) + " Islamic-finance function(s)'
new3 = '    findings_full = findings\n    findings = findings_full[:30]\n    return {"checked": True, "findings": findings, "total_findings": len(findings_full), "findings_shown": len(findings), "findings_truncated": len(findings_full) > 30, "summary": str(len(findings_full)) + " Islamic-finance function(s)'
results["3_riba"] = content.count(old3)
content = content.replace(old3, new3, 1)

# Fix 4: SBP circular reference
old4 = '    findings = findings[:30]\n    if functions_found == 0:'
new4 = '    findings_full = findings\n    findings = findings_full[:30]\n    if functions_found == 0:'
results["4a_sbp_capture"] = content.count(old4)
content = content.replace(old4, new4, 1)

old4b = '    return {"checked": True, "findings": findings, "functions_found": functions_found, "total_findings": len(findings), "summary": str(len(findings)) + " compliance function(s)'
new4b = '    return {"checked": True, "findings": findings, "functions_found": functions_found, "total_findings": len(findings_full), "findings_shown": len(findings), "findings_truncated": len(findings_full) > 30, "summary": str(len(findings_full)) + " compliance function(s)'
results["4b_sbp_use"] = content.count(old4b)
content = content.replace(old4b, new4b, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIX4BUGGY-DONE")