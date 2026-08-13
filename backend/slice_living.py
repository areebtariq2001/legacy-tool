with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
idx = content.find("def save_living_documentation")
idx_end = content.find("\ndef ", idx+10)
with open("living_full_slice.txt", "w", encoding="utf-8") as out:
    out.write(content[idx:idx_end])
print("DONE genuinely - length:", idx_end - idx)
