import re
with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

calls1 = len(re.findall(r'\bget_ai_response\(', content))
calls2 = len(re.findall(r'\bcall_ai_provider\(', content))

with open("check_ai_calls3_output.txt", "w", encoding="utf-8") as out:
    out.write("get_ai_response( appears: " + str(calls1) + " times (includes definition)\n")
    out.write("call_ai_provider( appears: " + str(calls2) + " times (includes definition)\n")

print("DONE")