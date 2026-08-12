with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('"executive-report", file.filename)')
chunk = content[idx-300:idx+100]

with open("zzz_execep_out.txt", "w", encoding="utf-8") as out:
    out.write(chunk)

print("DONE")