with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

import re
matches = re.findall(r'open\([^)]+\)', content)

with open("other_files_output2.txt", "w", encoding="utf-8") as out:
    for m in matches:
        out.write(m + "\n")

print("DONE - found", len(matches), "open() calls")