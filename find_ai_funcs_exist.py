with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("ai_funcs_exist_output.txt", "w", encoding="utf-8") as out:
    out.write("get_ai_response in file: " + str("get_ai_response" in content) + "\n")
    out.write("call_ai_provider in file: " + str("call_ai_provider" in content) + "\n")
    out.write("Count of 'get_ai_response': " + str(content.count("get_ai_response")) + "\n")
    out.write("Count of 'call_ai_provider': " + str(content.count("call_ai_provider")) + "\n")

print("DONE")