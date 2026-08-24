with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
anchor = '@app.post("/hidden-business-logic")'
c = content.count(anchor)
print("Anchor-count:", c)
code = 'def generate_compatibility_matrix(source, filename):\n    is_python = filename.lower().endswith(".py")\n    is_java = filename.lower().endswith(".java")\n    if not (is_python or is_java):\n        return {"matrix_generated": False, "targets": [], "matrix_summary": "Only Python/Java supported."}\n    targets = []\n    if is_python:\n        pairs = [("3.9", "3.12", ["distutils", "smtpd"])]\n        for fv, tv, removed in pairs:\n            found = [p for p in removed if re.search(r"\\b" + p + r"\\b", source)]\n            targets.append({"from_version": "Python " + fv, "to_version": "Python " + tv, "breaking_issues": found, "compatible": len(found) == 0})\n    else:\n        pairs = [("11", "21", ["SecurityManager"])]\n        for fv, tv, removed in pairs:\n            found = [p for p in removed if re.search(r"\\b" + p + r"\\b", source)]\n            targets.append({"from_version": "Java " + fv, "to_version": "Java " + tv, "breaking_issues": found, "compatible": len(found) == 0})\n    return {"matrix_generated": True, "targets": targets, "matrix_summary": str(len(targets)) + " version-pair(s) checked.", "matrix_disclaimer": "Curated, non-exhaustive set of documented breaking changes. Always test against your actual target runtime."}\n\n@app.post("/compatibility-matrix")\nasync def compatibility_matrix_endpoint(file: UploadFile = File(...)):\n    try:\n        content2 = await file.read()\n        source, error = safe_read_file(content2, file.filename)\n        if error:\n            return JSONResponse(status_code=400, content={"filename": file.filename, "error": error})\n        result = generate_compatibility_matrix(source, file.filename)\n        result["filename"] = file.filename\n        track_usage("compatibility-matrix", file.filename)\n        write_audit_log("compatibility-matrix", file.filename, "checked")\n        return result\n    except Exception as e:\n        return JSONResponse(status_code=400, content={"filename": file.filename, "error": "Compatibility matrix failed: " + str(e)})\n\n'
new_endpoint = code + anchor
if c == 1:
    content = content.replace(anchor, new_endpoint, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("COMPAT-MATRIX-DONE")
else:
    print("FAILED")