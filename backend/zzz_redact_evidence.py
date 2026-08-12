with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = "                if count == 1:\n                    _sample_line = ln.strip()[:120]"
new = "                if count == 1:\n                    _sample_line = re.sub(r'([=:]\\s*[\\\"\\x27])[^\\\"\\x27]+([\\\"\\x27])', r'\\1***REDACTED***\\2', ln.strip()[:150])"

total = content.count(old)
print("Occurrences found:", total)
if total >= 1:
    content = content.replace(old, new)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED - all occurrences replaced")
else:
    print("FAILED")