main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old7 = "result = suggest_github_issue_fix(issue_title, issue_body, source)"
new7 = "result = await run_in_threadpool(suggest_github_issue_fix, issue_title, issue_body, source)"
results["7_github_issue_fix"] = content.count(old7)
content = content.replace(old7, new7, 1)

old8 = "result = call_ai_provider(prompt, max_tokens=600)"
new8 = "result = await run_in_threadpool(call_ai_provider, prompt, 600)"
results["8_traceability_query"] = content.count(old8)
content = content.replace(old8, new8, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXTHREADPOOL78-DONE")