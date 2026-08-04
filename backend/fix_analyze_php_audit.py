with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    result = analyze_php(source)
    result["filename"] = file.filename
    track_usage("analyze-php", file.filename)
    return result'''

new = '''    result = analyze_php(source)
    result["filename"] = file.filename
    track_usage("analyze-php", file.filename)
    write_audit_log("analyze-php", file.filename, "issues=" + str(len(result.get("issues", []))))
    return result'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")