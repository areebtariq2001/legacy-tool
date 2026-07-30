with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.middleware("http")
async def cors_handler(request: Request, call_next):
    if request.method == "OPTIONS":
        return JSONResponse(
            content={},
            status_code=200,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS, PATCH",
                "Access-Control-Allow-Headers": "*",
                "Access-Control-Max-Age": "86400",
            }
        )
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS, PATCH"
    response.headers["Access-Control-Allow-Headers"] = "*"'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    print("Match found - showing what comes right after to check for safe cutoff point")
    idx = content.find(old)
    print(repr(content[idx+len(old):idx+len(old)+150]))
else:
    print("NOT FOUND - stopping safely, no changes made")