with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("check_ai_functions_output.txt", "w", encoding="utf-8") as out:
    out.write("call_groq exists: " + str("def call_groq" in content) + "\n")
    out.write("call_ollama exists: " + str("def call_ollama" in content) + "\n")
    out.write("ai_explain exists: " + str("def ai_explain" in content) + "\n")
    out.write("ai_generate_tests exists: " + str("def ai_generate_tests" in content) + "\n")

print("DONE")