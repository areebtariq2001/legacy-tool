main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old2 = "result = ai_suggest(source, detect_language(file.filename))"
new2 = "result = await run_in_threadpool(ai_suggest, source, detect_language(file.filename))"
results["2_ai_suggest"] = content.count(old2)
content = content.replace(old2, new2, 1)

old3 = "result = ai_explain(source, detect_language(file.filename))"
new3 = "result = await run_in_threadpool(ai_explain, source, detect_language(file.filename))"
results["3_ai_explain"] = content.count(old3)
content = content.replace(old3, new3, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIXTHREADPOOL23-DONE")