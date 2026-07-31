with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''    if not code_lines:
        if language == "python":
            return {
                "migrated_code": source, "ai_powered": True, "valid": True,
                "validation_message": "File has no executable code (empty or comments only).",
                "verified": True, "verify_message": "Nothing to verify - no executable code.",
                "vars_ok": True, "var_message": "", "confidence_score": 100,
                "confidence_level": "High confidence", "confidence_reason": "no executable code to migrate",
                "why_explanations": [], "dependencies": []
            }
        else:
            return {"migrated_code": source, "ai_powered": True,
                    "valid": True, "validation_message": "File has no executable code.",
                    "confidence_score": 100, "confidence_level": "High confidence",
                    "confidence_reason": "no executable code to migrate"}'''

new1 = '''    if not code_lines:
        if language == "python":
            return {
                "migrated_code": source, "ai_powered": True, "valid": True,
                "validation_message": "File has no executable code (empty or comments only).",
                "verified": True, "verify_message": "Nothing to verify - no executable code.",
                "vars_ok": True, "var_message": "", "confidence_score": None,
                "confidence_level": "Not Applicable", "confidence_reason": "No executable code was found to migrate, so a confidence score does not apply.",
                "why_explanations": [], "dependencies": []
            }
        else:
            return {"migrated_code": source, "ai_powered": True,
                    "valid": True, "validation_message": "File has no executable code.",
                    "confidence_score": None, "confidence_level": "Not Applicable",
                    "confidence_reason": "No executable code was found to migrate, so a confidence score does not apply."}'''

old2 = '''        f"Return ONLY the converted code, no explanations, no markdown.\\n\\n"
        f"Legacy code:\\n{source}"
    )'''

new2 = '''        f"Return ONLY the converted code, no explanations, no markdown.\\n\\n"
        f"Legacy code:\\n{source[:20000]}"
    )'''

count1 = content.count(old1)
count2 = content.count(old2)
print("Fix 1 (Bug 6) occurrences:", count1)
print("Fix 2 (Bug 10) occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Bug 6 PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Bug 10 PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")