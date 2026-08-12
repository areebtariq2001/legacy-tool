with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        result = generate_executive_report(source, file.filename)
        result["filename"] = file.filename
        track_usage("executive-report", file.filename)
        return result'''

new = '''        result = generate_executive_report(source, file.filename)
        result["filename"] = file.filename
        track_usage("executive-report", file.filename)
        write_audit_log("executive-report", file.filename, f"health={result.get('exec_health', 0)}")
        return result'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED")