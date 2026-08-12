with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
old = '"evidence": f"First occurrence at line {line_nums[0]}: {_sample_line}"'
count = content.count(old)
print("Occurrences found:", count)