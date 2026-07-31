with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

import re
calls1 = len(re.findall(r'\bget_ai_response\(', content))
calls2 = len(re.findall(r'\bcall_ai_provider\(', content))

with open("ai_funcs_calls_output.txt", "w", encoding="utf-8") as out:
    out.write("get_ai_response called: " + str(calls1) + " times\n")
    out.write("call_ai_provider called: " + str(calls2) + " times\n")

print("DONE")