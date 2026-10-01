main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old9 = "result = login_user(req.email, req.password, ip=_get_client_ip(request))"
new9 = "result = await run_in_threadpool(login_user, req.email, req.password, ip=_get_client_ip(request))"
results["9_login"] = content.count(old9)
content = content.replace(old9, new9, 1)

old10 = '''async def auth_register_endpoint(req: AuthRequest):
    result = register_user(req.email, req.password)'''
new10 = '''async def auth_register_endpoint(req: AuthRequest):
    result = await run_in_threadpool(register_user, req.email, req.password)'''
results["10_register"] = content.count(old10)
content = content.replace(old10, new10, 1)

old11a = '''async def save_approval_endpoint(request: Request, req: ApprovalRequest = None, filename: str = "unknown", decision: str = "Approved", reviewer_notes: str = "", action_type: str = "migration"):
    _user_email = _check_user_auth(request)'''
new11a = '''async def save_approval_endpoint(request: Request, req: ApprovalRequest = None, filename: str = "unknown", decision: str = "Approved", reviewer_notes: str = "", action_type: str = "migration"):
    _user_email = await run_in_threadpool(_check_user_auth, request)'''
results["11a_save_approval_auth"] = content.count(old11a)
content = content.replace(old11a, new11a, 1)

old11b = "result = save_approval_decision(filename, decision, reviewer_notes, action_type, approved_by=_user_email)"
new11b = "result = await run_in_threadpool(save_approval_decision, filename, decision, reviewer_notes, action_type, approved_by=_user_email)"
results["11b_save_approval_decision"] = content.count(old11b)
content = content.replace(old11b, new11b, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXTHREADPOOL9TO11-DONE")