with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

checks = [
    ('return {"filename": file.filename, "error": f"Business rule extraction failed safely: {e}"}', "extract-business-rules"),
    ('return {"filename": file.filename, "error": f"Executive report failed safely: {e}"}', "executive-report"),
    ('return {"filename": file.filename, "error": f"Impact analysis failed safely: {e}"}', "analyze-impact"),
    ('return {"filename": file.filename, "error": f"Transaction flow mapping failed safely: {e}"}', "map-transaction-flow"),
    ('return {"filename": file.filename, "error": f"Rollback plan failed safely: {e}"}', "rollback-plan"),
]

with open("zzz_except_status_out.txt", "w") as out:
    for pattern, name in checks:
        count = content.count(pattern)
        out.write(name + " : bare-dict-no-status-code, count=" + str(count) + "\n")

print("DONE")