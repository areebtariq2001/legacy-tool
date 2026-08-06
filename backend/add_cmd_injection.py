with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''(r"(?i)\\+\\s*(request|input|params|argv)", "Possible SQL/command injection (concatenated user input)", "High"),'''
new = old + '''
    (r"(?i)\\b(os\\.system|subprocess\\.(call|run|Popen))\\s*\\([^)]*\\+", "Possible command injection (shell command built with + concatenation)", "High"),'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")