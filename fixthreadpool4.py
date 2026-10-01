main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = "result = ai_generate_tests(source, _gt_lang)"
new = "result = await run_in_threadpool(ai_generate_tests, source, _gt_lang)"

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXTHREADPOOL4-DONE")
else:
    print("FAILED - count was:", count)