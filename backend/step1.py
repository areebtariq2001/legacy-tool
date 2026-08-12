with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old1 = "is_working = \"not reachable\" not in result and \"error\" not in result.lower()"
new1 = "is_working = \"not reachable\" not in result and not result.lower().startswith(\"error\")"
c1 = content.count(old1)
if c1 == 1:
    content = content.replace(old1, new1, 1)
with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
with open("step1_log.txt", "w") as log:
    log.write("Step1 count: " + str(c1))
print("STEP1 DONE")
