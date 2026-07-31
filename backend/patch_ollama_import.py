with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''def call_ollama(prompt):
    import requests as _req
    try:
        r = _req.post(os.environ.get("OLLAMA_URL", "http://localhost:11434") + "/api/generate", json={"model": "codellama:13b", "prompt": prompt, "stream": False}, timeout=180)'''

new = '''def call_ollama(prompt):
    try:
        r = requests.post(os.environ.get("OLLAMA_URL", "http://localhost:11434") + "/api/generate", json={"model": "codellama:13b", "prompt": prompt, "stream": False}, timeout=15)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")