with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = "from datetime import datetime, timedelta\nimport secrets, timedelta\nimport secrets\n"
c = content.count(old)
with open("remove_bad_line_count.txt", "w") as log:
    log.write("count: " + str(c))
if c == 1:
    new = "from datetime import datetime, timedelta\nimport secrets\n"
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
print("REMOVEBAD DONE")
