with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
r1 = ('        result = map_regional_compliance(source, file.filename, region)\n        result["filename"] = file.filename\n        track_usage("regional-compliance", file.filename)\n        return result', '        result = map_regional_compliance(source, file.filename, region)\n        result["filename"] = file.filename\n        track_usage("regional-compliance", file.filename)\n        write_audit_log("regional-compliance", file.filename, "region=" + region)\n        return result')
total = 0
if content.count(r1[0]) == 1:
    content = content.replace(r1[0], r1[1], 1)
    total = total + 1
with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)
msg = "DONE total=" + str(total)
print(msg)