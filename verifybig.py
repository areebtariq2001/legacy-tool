main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifybig_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. sanitize_ai_output function ===\n")
    idx1 = content.find("def sanitize_ai_output")
    idx1_end = content.find("\ndef ", idx1+20)
    out.write(content[idx1:idx1_end] + chr(10) + chr(10))

    out.write("=== 2. urllib import check ===\n")
    out.write("'import urllib' count: " + str(content.count("import urllib")) + chr(10))
    out.write("'urlparse(' count: " + str(content.count("urlparse(")) + chr(10) + chr(10))

    out.write("=== 4. rate limit endpoint keys ===\n")
    idx4 = content.find("_ENDPOINT_SPECIFIC_LIMITS = {")
    idx4_end = content.find("}", idx4)
    out.write(content[idx4:idx4_end+1] + chr(10) + chr(10))
    out.write("'/auth/login' route exists: " + str('"/auth/login"' in content or "'/auth/login'" in content) + chr(10))
    out.write("'@app.post(\"/login\"' exists: " + str('@app.post("/login"' in content) + chr(10))
    idx4b = content.find('@app.post("/login"')
    if idx4b == -1:
        idx4b = content.find("login")
    out.write(content[max(0,idx4b-50):idx4b+100] if idx4b!=-1 else "not found")
print("VERIFYBIG-DONE")