main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkgroqmodel_result.txt", "w", encoding="utf-8") as out:
    idx = content.find("groq.com")
    out.write("groq.com-found-at-index: " + str(idx) + chr(10))
    if idx != -1:
        out.write(content[idx:idx+500] + chr(10) + chr(10))
    idx2 = content.find("gpt-oss")
    out.write("gpt-oss-string-found: " + str(idx2 != -1) + chr(10))
    if idx2 != -1:
        out.write(content[max(0,idx2-100):idx2+100])
print("CHECKGROQMODEL-DONE")