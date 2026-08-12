with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old4 = "async def code_qa_endpoint(file: UploadFile = File(...), question: str = \"What does this code do?\"):\n    try:\n        content = await file.read()"
new4 = "async def code_qa_endpoint(file: UploadFile = File(...), question: str = \"What does this code do?\"):\n    try:\n        if len(question) > 500:\n            return JSONResponse(status_code=400, content={\"filename\": file.filename, \"error\": \"Question too long\"})\n        question = question.strip()\n        content = await file.read()"
c4 = content.count(old4)
if c4 == 1:
    content = content.replace(old4, new4, 1)
with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
with open("step4_log.txt", "w") as log:
    log.write("Step4 count: " + str(c4))
print("STEP4 DONE")
