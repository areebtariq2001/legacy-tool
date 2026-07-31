with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("check_ai_functions_output2.txt", "w", encoding="utf-8") as out:
    out.write("get_ai_response defined: " + str("def get_ai_response" in content) + "\n")
    out.write("call_ai_provider defined: " + str("def call_ai_provider" in content) + "\n")
    out.write("call_groq defined: " + str("def call_groq" in content) + "\n")
    out.write("call_ollama defined: " + str("def call_ollama" in content) + "\n")

print("DONE")