with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = "except Exception as e:\n            return {\"error\": str(e), \"history\": []}"
c = content.count(old)
with open("revert_count.txt", "w") as log:
    log.write("count: " + str(c))
if c == 1:
    new = "except Exception:\n            return []"
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
print("REVERT DONE")
