with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.middleware("http")'''

new = '''# Note: CORSMiddleware intentionally NOT used here - the custom cors_handler
# below already sets all needed CORS headers on every request (including
# OPTIONS preflight), so adding CORSMiddleware as well would set duplicate
# headers on every response.
@app.middleware("http")'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")