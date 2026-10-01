main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '''@app.post("/auth/register")
async def auth_register_endpoint(req: AuthRequest):
    result = register_user(req.email, req.password)
    if not result.get("success"):
        return JSONResponse(status_code=400, content=result)
    return result'''

new = '''@app.post("/auth/register")
async def auth_register_endpoint(req: AuthRequest):
    result = register_user(req.email, req.password)
    if not result.get("success"):
        return JSONResponse(status_code=400, content=result)
    return result


@app.post("/auth/logout")
async def auth_logout_endpoint(request: Request):
    token = request.headers.get("x-session-token", "")
    if not token or len(token) > 200:
        return {"success": True}
    conn = _get_db_connection()
    if not conn:
        return {"success": True}
    cur = None
    try:
        cur = conn.cursor()
        cur.execute("DELETE FROM sessions WHERE token = %s", (token,))
        conn.commit()
        return {"success": True}
    except Exception:
        return {"success": True}
    finally:
        if cur:
            cur.close()
        conn.close()'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("ADDLOGOUT-DONE")
else:
    print("FAILED - count was:", count)