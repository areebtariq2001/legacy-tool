with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

import re
endpoints = ["analyze-php", "migrate-php", "analyze-java", "migrate-java", "analyze-cobol", "migrate-cobol"]
lines = content.split("\n")

with open("all_lang_endpoints_output.txt", "w", encoding="utf-8") as out:
    for ep in endpoints:
        for i, line in enumerate(lines):
            if '"/' + ep + '"' in line:
                snippet = "\n".join(lines[i:i+6])
                uses_safe_read = "safe_read_file" in snippet
                out.write(ep + " uses safe_read_file: " + str(uses_safe_read) + "\n")
                break

print("DONE")