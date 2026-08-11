with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    return {
        "ai_native_score": score,
        "ai_native_level": level,
        "ai_native_findings": findings,
        "ai_native_disclaimer": "Heuristic check of how ready this code is to integrate with modern AI/analytics systems (modularity, config, logging, safety, types). A guide for modernization planning, not a guarantee."
    }'''

new = '''    return {
        "ai_native_score": score,
        "ai_native_level": level,
        "ai_native_findings": findings,
        "ai_native_summary": f"AI-Native readiness: {score}/100 ({level}) - {len(findings)} issue(s) found",
        "ai_native_disclaimer": "Heuristic check of how ready this code is to integrate with modern AI/analytics systems (modularity, config, logging, safety, types). A guide for modernization planning, not a guarantee."
    }'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")