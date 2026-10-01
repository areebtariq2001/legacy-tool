main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

# ai_suggest
old1 = '''    if result.startswith("AI_ERROR") or result.startswith("AI service error"):
        return {"suggestions": None, "error": result, "injection_attempt_flagged": _injection_flagged}
    return {"suggestions": result, "injection_attempt_flagged": _injection_flagged}'''
new1 = '''    if result.startswith("AI_ERROR") or result.startswith("AI service error"):
        return {"suggestions": None, "error": result, "injection_attempt_flagged": _injection_flagged}
    return {"suggestions": sanitize_ai_output(result), "injection_attempt_flagged": _injection_flagged}'''
results["1_ai_suggest"] = content.count(old1)
content = content.replace(old1, new1, 1)

# ai_explain
old2 = '''    if result.startswith("AI_ERROR") or result.startswith("AI service error"):
        return {"explanation": None, "error": result, "injection_attempt_flagged": _injection_flagged}
    return {"explanation": result, "injection_attempt_flagged": _injection_flagged}'''
new2 = '''    if result.startswith("AI_ERROR") or result.startswith("AI service error"):
        return {"explanation": None, "error": result, "injection_attempt_flagged": _injection_flagged}
    return {"explanation": sanitize_ai_output(result), "injection_attempt_flagged": _injection_flagged}'''
results["2_ai_explain"] = content.count(old2)
content = content.replace(old2, new2, 1)

# ai_generate_tests
old3 = '''    if result.startswith("AI_ERROR") or result.startswith("AI service error"):
        return {"tests": None, "error": result, "injection_attempt_flagged": _injection_flagged}
    return {"tests": result, "injection_attempt_flagged": _injection_flagged}'''
new3 = '''    if result.startswith("AI_ERROR") or result.startswith("AI service error"):
        return {"tests": None, "error": result, "injection_attempt_flagged": _injection_flagged}
    return {"tests": sanitize_ai_output(result), "injection_attempt_flagged": _injection_flagged}'''
results["3_ai_generate_tests"] = content.count(old3)
content = content.replace(old3, new3, 1)

# answer_code_question
old4 = '''    if _injection_flagged:
        write_audit_log("security-flag", filename, "possible prompt injection pattern detected in question/source")
    return {"question": question, "answer": answer, "qa_disclaimer": "AI-generated answer based on the uploaded file only. Always verify against the actual code and consult the original developers where possible.", "injection_attempt_flagged": _injection_flagged}'''
new4 = '''    if _injection_flagged:
        write_audit_log("security-flag", filename, "possible prompt injection pattern detected in question/source")
    return {"question": question, "answer": sanitize_ai_output(answer), "qa_disclaimer": "AI-generated answer based on the uploaded file only. Always verify against the actual code and consult the original developers where possible.", "injection_attempt_flagged": _injection_flagged}'''
results["4_answer_code_question"] = content.count(old4)
content = content.replace(old4, new4, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("APPLY-SANITIZATION-DONE")