with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '@app.post("/analyze")'
new = '''@app.get("/health")
def health():
    return {"status": "ok", "version": "1.0"}

@app.post("/analyze")'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - trying alternate anchor")