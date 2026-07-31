with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def get_ai_response(prompt):
    provider = os.environ.get("AI_PROVIDER", "groq").lower()
    if provider == "ollama":
        result = call_ollama(prompt)
        if "not reachable" not in result and "error" not in result.lower()[:50]:
            return result
        return call_groq(prompt)
    return call_groq(prompt)

'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, "", 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY - removed dead code")
else:
    print("FAILED - aborting to be safe, exact text did not match")