main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.post("/scan-repo")
async def scan_repo_endpoint(req: RepoRequest):'''
new = '''def _scan_repo_blocking(req: RepoRequest):'''

count = content.count(old)
print("Decorator+def occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    # Now insert the new thin async wrapper right before the renamed function
    idx = content.find("def _scan_repo_blocking(req: RepoRequest):")
    wrapper = '''@app.post("/scan-repo")
async def scan_repo_endpoint(req: RepoRequest):
    return await run_in_threadpool(_scan_repo_blocking, req)


'''
    content = content[:idx] + wrapper + content[idx:]
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXSCANREPO-DONE")
else:
    print("FAILED - count was:", count)