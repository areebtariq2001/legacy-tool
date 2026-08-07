with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''(r"(?i)\\b(os\\.system|subprocess\\.(call|run|Popen))\\s*\\([^)]*\\+", "Possible command injection (shell command built with + concatenation)", "High"),'''
new = old + '''
    (r"(?i)\\b(system|exec|passthru|shell_exec|popen|proc_open)\\s*\\([^)]*\\.\\s*\\$", "Possible command injection (PHP shell command built with . concatenation)", "High"),'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")