with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''@app.post("/save-approval")
async def save_approval_endpoint(filename: str = "unknown", decision: str = "Approved", reviewer_notes: str = "", action_type: str = "migration"):
    try:
        result = save_approval_decision(filename, decision, reviewer_notes, action_type)
        return result
    except Exception as e:
        return {"error": "Approval save failed safely: " + str(e)}'''

new1 = '''@app.post("/save-approval")
async def save_approval_endpoint(request: Request, filename: str = "unknown", decision: str = "Approved", reviewer_notes: str = "", action_type: str = "migration"):
    _user_email = _check_user_auth(request)
    if not _user_email:
        return JSONResponse(status_code=401, content={"error": "Unauthorized - please log in to approve or reject migrations"})
    try:
        result = save_approval_decision(filename, decision, reviewer_notes, action_type)
        result["approved_by"] = _user_email
        return result
    except Exception as e:
        return {"error": "Approval save failed safely: " + str(e)}'''

old2 = '''@app.get("/approval-history")
async def approval_history_endpoint():
    try:
        history = get_approval_history()
        return {"approval_history": history, "total_decisions": len(history)}
    except Exception as e:
        return {"error": "Could not load approval history: " + str(e)}'''

new2 = '''@app.get("/approval-history")
async def approval_history_endpoint(request: Request):
    _user_email = _check_user_auth(request)
    if not _user_email:
        return JSONResponse(status_code=401, content={"error": "Unauthorized - please log in to view approval history"})
    try:
        history = get_approval_history()
        return {"approval_history": history, "total_decisions": len(history)}
    except Exception as e:
        return {"error": "Could not load approval history: " + str(e)}'''

c1 = content.count(old1)
c2 = content.count(old2)
print("Occurrences 1:", c1)
print("Occurrences 2:", c2)

if c1 == 1:
    content = content.replace(old1, new1, 1)
if c2 == 1:
    content = content.replace(old2, new2, 1)

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("DONE genuinely")