with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''def ai_suggest(source, language):
    _src_truncated = source[:8000]'''

new1 = '''def ai_suggest(source, language):
    language = re.sub(r"[\\r\\n]", " ", str(language))[:50].strip()
    if not language:
        language = "code"
    _src_truncated = source[:8000]'''

old2 = '''def ai_explain(source, language):
    _src_truncated = source[:8000]'''

new2 = '''def ai_explain(source, language):
    language = re.sub(r"[\\r\\n]", " ", str(language))[:50].strip()
    if not language:
        language = "code"
    _src_truncated = source[:8000]'''

count1 = content.count(old1)
count2 = content.count(old2)
print("ai_suggest fix occurrences:", count1)
print("ai_explain fix occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("ai_suggest PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("ai_explain PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")