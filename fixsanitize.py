main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = 'text = re.sub(r\'on\\w+\\s*=\\s*["\\x27][^"\\x27]*["\\x27]\', "", text, flags=re.IGNORECASE)'
new = 'text = re.sub(r\'\\bon(?:click|load|error|mouseover|mouseout|focus|blur|submit|change|keydown|keyup|keypress|mousedown|mouseup|dblclick|contextmenu|drag|drop|scroll|resize|abort|beforeunload|hashchange|input|invalid|toggle|wheel)\\s*=\\s*["\\x27][^"\\x27]*["\\x27]\', "", text, flags=re.IGNORECASE)'

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIXSANITIZE-DONE")
else:
    print("FAILED - count was:", count)