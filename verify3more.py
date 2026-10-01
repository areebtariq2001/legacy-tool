main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verify3more_result.txt", "w", encoding="utf-8") as out:
    out.write("=== urllib import lines ===\n")
    for line in content.split(chr(10)):
        if "import urllib" in line:
            out.write(line + chr(10))
    out.write(chr(10))

    out.write("=== has_key related code ===\n")
    idx = content.find("has_key")
    if idx != -1:
        out.write(content[max(0,idx-200):idx+300] + chr(10) + chr(10))
    else:
        out.write("NOT-FOUND" + chr(10) + chr(10))

    out.write("=== actual login route decorator ===\n")
    idx2 = content.find('@app.post(') 
    while idx2 != -1:
        snippet = content[idx2:idx2+40]
        if "login" in snippet.lower():
            out.write(snippet + chr(10))
        idx2 = content.find('@app.post(', idx2+1)
print("VERIFY3MORE-DONE")