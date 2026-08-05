with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old1 = '''    result = analyze_java(source)
    result["filename"] = file.filename
    track_usage("analyze-java", file.filename)
    return result'''
new1 = '''    result = analyze_java(source)
    result["filename"] = file.filename
    track_usage("analyze-java", file.filename)
    write_audit_log("analyze-java", file.filename, "issues=" + str(len(result.get("issues", []))))
    return result'''

old2 = '''    result = analyze_cobol(source)
    result["filename"] = file.filename
    track_usage("analyze-cobol", file.filename)
    return result'''
new2 = '''    result = analyze_cobol(source)
    result["filename"] = file.filename
    track_usage("analyze-cobol", file.filename)
    write_audit_log("analyze-cobol", file.filename, "issues=" + str(len(result.get("issues", []))))
    return result'''

count1 = content.count(old1)
count2 = content.count(old2)
print("analyze-java fix occurrences:", count1)
print("analyze-cobol fix occurrences:", count2)

if count1 == 1:
    content = content.replace(old1, new1, 1)
    print("analyze-java PATCHED")
if count2 == 1:
    content = content.replace(old2, new2, 1)
    print("analyze-cobol PATCHED")

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
print("FILE SAVED")