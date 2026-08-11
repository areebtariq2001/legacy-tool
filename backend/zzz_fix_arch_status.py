with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

idx = content.find('"generate-architecture"')
chunk = content[idx:idx+700]

with open("zzz_arch_chunk.txt", "w", encoding="utf-8") as out:
    out.write(chunk)

print("DONE")