with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = "@app.post(\"/save-approval\")\nasync def save_approval_endpoint(request: Request, filename: str = \"unknown\", decision: str = \"Approved\", reviewer_notes: str = \"\", action_type: str = \"migration\"):"
c = content.count(old)
with open("bug4_precheck3.txt", "w") as log:
    log.write("count: " + str(c))
print("PRECHECK DONE")
