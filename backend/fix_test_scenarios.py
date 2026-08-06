with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    ai_response = call_ai_provider(prompt, max_tokens=500)
    scenarios = []
    for line in ai_response.split("\\n"):
        line = line.strip()
        if line.startswith("TEST:") and "INPUT:" in line and "EXPECTED:" in line:
            try:
                func = line.split("TEST:")[1].split("|")[0].strip()
                inp = line.split("INPUT:")[1].split("|")[0].strip()
                exp = line.split("EXPECTED:")[1].strip()
                scenarios.append({"function": func, "input": inp, "expected": exp})
            except:
                pass
    return {
        "test_scenarios": scenarios,
        "scenarios_note": "AI-suggested test scenarios to help verify behavioral parity. Review and adapt before use as formal tests."
    }'''

new = '''    ai_response = call_ai_provider(prompt, max_tokens=800)
    if ai_response.startswith("AI_ERROR") or ai_response.startswith("AI service error"):
        return {"test_scenarios": [], "error": ai_response, "scenarios_note": "AI service is temporarily unavailable - could not generate test scenarios."}
    scenarios = []
    for line in ai_response.split("\\n"):
        line = line.strip()
        if line.startswith("TEST:") and "INPUT:" in line and "EXPECTED:" in line:
            try:
                func = line.split("TEST:")[1].split("|")[0].strip()
                inp = line.split("INPUT:")[1].split("|")[0].strip()
                exp = line.split("EXPECTED:")[1].strip()
                scenarios.append({"function": func, "input": inp, "expected": exp})
            except Exception:
                pass
    return {
        "test_scenarios": scenarios,
        "scenarios_note": "AI-suggested test scenarios to help verify behavioral parity. Review and adapt before use as formal tests."
    }'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")