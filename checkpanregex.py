main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find("card.?number|cvv")
with open("checkpanregex_result.txt", "w", encoding="utf-8") as out:
    if idx != -1:
        out.write("Genuinely-EXACT-REPR: " + repr(content[max(0,idx-20):idx+40]))
    else:
        out.write("PATTERN-NOT-FOUND-with-this-search")
print("CHECKPANREGEX-DONE")