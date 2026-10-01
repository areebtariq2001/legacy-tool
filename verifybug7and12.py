main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("verifybug7and12_result.txt", "w", encoding="utf-8") as out:
    out.write("=== 7. py_issue_checks pattern-matching logic ===\n")
    idx = content.find("py_issue_checks")
    idx_end = content.find("\ndef ", idx)
    if idx_end == -1 or idx_end - idx > 3000:
        idx_end = idx + 2000
    body = content[idx:idx_end]
    for line in body.split(chr(10)):
        if "pattern in" in line or "for pattern" in line:
            out.write(line.strip() + chr(10))
    out.write(chr(10))

    out.write("=== 12. endpoints returning plain dict without JSONResponse on error ===\n")
    for ep in ["/ai-native-readiness", "/predict-risk", "/cicd", "/db-schema", "/api-deps"]:
        idx2 = content.find('"' + ep + '"')
        if idx2 != -1:
            idx2_end = content.find("\n@app.", idx2)
            body2 = content[idx2:idx2_end][:600]
            out.write("--- " + ep + " ---\n")
            has_jsonresponse_on_error = "JSONResponse" in body2 and "error" in body2
            out.write("has-JSONResponse-with-error: " + str(has_jsonresponse_on_error) + chr(10))
        else:
            out.write("--- " + ep + " NOT-FOUND ---\n")
print("VERIFYBUG7AND12-DONE")