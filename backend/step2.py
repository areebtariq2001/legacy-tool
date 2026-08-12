with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old2 = "async def local_ai_status_endpoint():\n    result = call_ollama"
new2 = "async def local_ai_status_endpoint(request: Request):\n    if not _check_admin_auth(request):\n        return JSONResponse(status_code=401, content={\"error\": \"Unauthorized\"})\n    result = call_ollama"
c2 = content.count(old2)
if c2 == 1:
    content = content.replace(old2, new2, 1)
with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
with open("step2_log.txt", "w") as log:
    log.write("Step2 count: " + str(c2))
print("STEP2 DONE")
