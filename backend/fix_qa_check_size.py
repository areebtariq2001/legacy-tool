with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.post("/qa-check")
async def qa_check(req: QARequest):
    try:
        result = ai_qa_compare(req.original, req.migrated)'''

new = '''@app.post("/qa-check")
async def qa_check(req: QARequest):
    if len(req.original) > 50000 or len(req.migrated) > 50000:
        return {"qa_verdict": "ERROR", "qa_full_response": "Input too large for QA check (max 50,000 characters per field)."}
    try:
        result = ai_qa_compare(req.original, req.migrated)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")