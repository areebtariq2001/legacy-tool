with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

# Fix Bug 6: remove redundant import
old1 = '''def get_ai_response(prompt):
    import os as _os
    provider = _os.environ.get("AI_PROVIDER", "groq").lower()'''
new1 = '''def get_ai_response(prompt):
    provider = os.environ.get("AI_PROVIDER", "groq").lower()'''

count1 = content.count(old1)
print("Bug 6 occurrences found:", count1)
if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("Bug 6 PATCHED")
else:
    print("Bug 6 FAILED - skipping")

# Fix Bug 11: add API key check
old2 = '''def call_groq(prompt, max_tokens=500):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    try:'''
new2 = '''def call_groq(prompt, max_tokens=500):
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
    if not GROQ_API_KEY:
        return "AI_ERROR: GROQ_API_KEY is not configured on the server."
    try:'''

count2 = content.count(old2)
print("Bug 11 occurrences found:", count2)
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("Bug 11 PATCHED")
else:
    print("Bug 11 FAILED - skipping")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

print("FILE SAVED")