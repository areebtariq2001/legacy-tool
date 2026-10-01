main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkregister_result.txt", "w", encoding="utf-8") as out:
    idx = content.find('@app.post(')
    while idx != -1:
        snippet = content[idx:idx+40]
        if "register" in snippet.lower():
            out.write(snippet + chr(10))
        idx = content.find('@app.post(', idx+1)

    out.write(chr(10) + "=== urlparse usage in scan_repo_endpoint ===\n")
    idx2 = content.find("def scan_repo_endpoint")
    idx2_end = content.find("\ndef ", idx2+20)
    body2 = content[idx2:idx2_end]
    idx3 = body2.find("urlparse")
    if idx3 != -1:
        out.write(body2[max(0,idx3-100):idx3+150])
    else:
        out.write("urlparse-NOT-found-in-this-function")
print("CHECKREGISTER-DONE")