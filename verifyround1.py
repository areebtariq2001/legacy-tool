main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifyround1_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 1. scan-repo disclaimer ===\n")
    idx1 = content.find("def scan_repo_endpoint")
    idx1_end = content.find("\ndef ", idx1+20)
    body1 = content[idx1:idx1_end]
    idx1b = body1.find("disclaimer")
    if idx1b != -1:
        out.write(body1[max(0,idx1b-100):idx1b+200] + chr(10) + chr(10))
    else:
        out.write("no-disclaimer-field-found-in-scan_repo_endpoint" + chr(10) + chr(10))

    out.write("=== 2. previous_content full context ===\n")
    idx2 = content.find("previous_content")
    idx2_start = content.rfind("def ", 0, idx2)
    out.write(content[idx2_start:idx2+250] + chr(10) + chr(10))

    out.write("=== 3. _verify_security_log_integrity 200-truncation ===\n")
    idx3 = content.find("del _security_log[200:]")
    out.write("Found: " + str(idx3 != -1) + chr(10))

    out.write(chr(10) + "=== 4. count of @app routes with auth check nearby ===\n")
    import re as re_mod
    all_routes = re_mod.findall(r'@app\.(get|post|put|delete)\("([^"]+)"\)', content)
    out.write("Total-routes: " + str(len(all_routes)) + chr(10))
    out.write("_check_user_auth-occurrences: " + str(content.count("_check_user_auth(")) + chr(10))
    out.write("_check_admin_auth-occurrences: " + str(content.count("_check_admin_auth(")))
print("VERIFYROUND1-DONE")