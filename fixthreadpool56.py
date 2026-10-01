main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old5 = "result = generate_documentation(source, file.filename)"
new5 = "result = await run_in_threadpool(generate_documentation, source, file.filename)"
results["5_generate_docs"] = content.count(old5)
content = content.replace(old5, new5, 1)

old6 = "result = verify_ai_output_consistency(source, language)"
new6 = "result = await run_in_threadpool(verify_ai_output_consistency, source, language)"
results["6_ai_consistency"] = content.count(old6)
content = content.replace(old6, new6, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXTHREADPOOL56-DONE")