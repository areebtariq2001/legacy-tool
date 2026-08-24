with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    phase_list = []
    for i, fns in enumerate(phases):
        risk = "Low" if i == 0 else "Medium" if i < len(phases) - 1 else "High"
        reasoning = "No dependencies on other in-file functions - safest starting point, extract/migrate first." if i == 0 else (
            "Depends only on already-migrated functions from earlier phases - safe to proceed once those are done." if i < len(phases) - 1 else
            "Foundational/widely-depended-upon functions - migrate last, with the most test coverage, since changes here have the widest blast radius."
        )
        phase_list.append({"phase": i + 1, "functions": fns, "function_count": len(fns), "risk_level": risk, "reasoning": reasoning})
    return {"plan_generated": True, "phases": phase_list, "total_phases": len(phase_list), "plan_summary": f"{len(phase_list)}-phase dependency-ordered migration sequence generated for {len(edges)} function(s), based on actual in-file call relationships.", "plan_disclaimer": "Ordering is based on static call-graph analysis within this single file only - does not account for cross-file dependencies, external callers, or business priority. A starting sequence, not a mandate."}'''

new = '''    security_findings = scan_sensitive_data(source).get("findings", [])
    security_lines = set()
    for f in security_findings:
        for ln in str(f.get("lines", "")).split(","):
            ln = ln.strip()
            if ln.isdigit():
                security_lines.add(int(ln))
    def _fn_touches_security(fn_name):
        _body, _start_line = _get_func_body_with_line(source, fn_name, filename)
        if _start_line == -1:
            return False
        _body_line_count = _body.count(chr(10))
        return any(_start_line <= ln <= _start_line + _body_line_count for ln in security_lines)
    phase_list = []
    for i, fns in enumerate(phases):
        risk = "Low" if i == 0 else "Medium" if i < len(phases) - 1 else "High"
        reasoning = "No dependencies on other in-file functions - safest starting point, extract/migrate first." if i == 0 else (
            "Depends only on already-migrated functions from earlier phases - safe to proceed once those are done." if i < len(phases) - 1 else
            "Foundational/widely-depended-upon functions - migrate last, with the most test coverage, since changes here have the widest blast radius."
        )
        function_details = []
        for fn in fns:
            touches_sec = _fn_touches_security(fn)
            function_details.append({"name": fn, "extra_caution": touches_sec, "note": "Contains security-sensitive code nearby - extra review recommended despite phase-level dependency risk." if touches_sec else None})
        phase_list.append({"phase": i + 1, "functions": fns, "function_details": function_details, "function_count": len(fns), "risk_level": risk, "reasoning": reasoning})
    return {"plan_generated": True, "phases": phase_list, "total_phases": len(phase_list), "plan_summary": f"{len(phase_list)}-phase dependency-ordered migration sequence generated for {len(edges)} function(s), based on actual in-file call relationships.", "plan_disclaimer": "Ordering is purely based on static call-graph dependency analysis within this single file - it does NOT factor in security risk when assigning phases. Functions flagged with extra_caution contain security-sensitive code nearby and deserve additional review regardless of their dependency-based phase. Does not account for cross-file dependencies, external callers, or business priority. A starting sequence, not a mandate."}'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")