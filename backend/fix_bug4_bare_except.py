with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        try:
            if line.startswith("["):
                entry["timestamp"] = line.split("]")[0][1:]
            if "action=" in line:
                entry["action"] = line.split("action=")[1].split(" |")[0].strip()
            if "file=" in line:
                entry["file"] = line.split("file=")[1].split(" |")[0].strip()
        except:
            pass
        entries.append(entry)'''

new = '''        try:
            if line.startswith("["):
                entry["timestamp"] = line.split("]")[0][1:]
            if "action=" in line:
                entry["action"] = line.split("action=")[1].split(" |")[0].strip()
            if "file=" in line:
                entry["file"] = line.split("file=")[1].split(" |")[0].strip()
        except Exception as e:
            entry["parse_error"] = str(e)
        entries.append(entry)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - trying to find exact text")