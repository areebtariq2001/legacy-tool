with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = 'if error:\n            return {"filename": file.filename, "error": error}'
new = 'if error:\n            return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})'

count = content.count(old)
print("Occurrences found:", count)
content = content.replace(old, new)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED - all occurrences replaced")