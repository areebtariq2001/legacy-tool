with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

target_line_num = 91
idx = target_line_num - 1

print("Current line 91:", repr(lines[idx]))

old_str = 'http://localhost:11434/api/generate'
if old_str in lines[idx]:
    lines[idx] = lines[idx].replace(
        '_req.post("http://localhost:11434/api/generate"',
        '_req.post(_os.environ.get("OLLAMA_URL", "http://localhost:11434") + "/api/generate"'
    )
    with open("main.py", "w", encoding="utf-8") as f:
        f.writelines(lines)
    print("PATCHED SUCCESSFULLY")
else:
    print("MISMATCH")