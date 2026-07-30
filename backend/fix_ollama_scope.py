with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = 'r = _req.post(_os.environ.get("OLLAMA_URL", "http://localhost:11434") + "/api/generate"'
new = 'r = _req.post(os.environ.get("OLLAMA_URL", "http://localhost:11434") + "/api/generate"'

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")