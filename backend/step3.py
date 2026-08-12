with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old3 = "async def regulatory_framework_endpoint(file: UploadFile = File(...), framework: str = \"SBP\"):\n    try:\n        content = await file.read()"
new3 = "async def regulatory_framework_endpoint(file: UploadFile = File(...), framework: str = \"SBP\"):\n    try:\n        _allowed_fw = {\"SBP\", \"Basel III\", \"PCI-DSS\", \"GDPR\"}\n        if framework not in _allowed_fw:\n            return JSONResponse(status_code=400, content={\"filename\": file.filename, \"error\": \"Invalid framework\"})\n        content = await file.read()"
c3 = content.count(old3)
if c3 == 1:
    content = content.replace(old3, new3, 1)
with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
with open("step3_log.txt", "w") as log:
    log.write("Step3 count: " + str(c3))
print("STEP3 DONE")
