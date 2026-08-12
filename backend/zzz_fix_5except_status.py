with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('return {"filename": file.filename, "error": f"Business rule extraction failed safely: {e}"}',
     'return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Business rule extraction failed safely: {e}"})'),
    ('return {"filename": file.filename, "error": f"Executive report failed safely: {e}"}',
     'return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Executive report failed safely: {e}"})'),
    ('return {"filename": file.filename, "error": f"Impact analysis failed safely: {e}"}',
     'return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Impact analysis failed safely: {e}"})'),
    ('return {"filename": file.filename, "error": f"Transaction flow mapping failed safely: {e}"}',
     'return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Transaction flow mapping failed safely: {e}"})'),
    ('return {"filename": file.filename, "error": f"Rollback plan failed safely: {e}"}',
     'return JSONResponse(status_code=400, content={"filename": file.filename, "error": f"Rollback plan failed safely: {e}"})'),
]

total = 0
with open("zzz_5except_fix_log.txt", "w") as log:
    for old, new in replacements:
        count = content.count(old)
        log.write(str(count) + " : " + old[:50] + "\n")
        if count == 1:
            content = content.replace(old, new, 1)
            total += 1

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("DONE - total patched:", total, "of 5")