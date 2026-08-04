with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

output_lines = []
for i, line in enumerate(lines):
    if "call_groq(" in line and "def call_groq" not in line and "def call_ai_provider" not in line:
        output_lines.append(str(i + 1) + ": " + line)

with open("all_call_groq_output.txt", "w", encoding="utf-8") as out:
    out.writelines(output_lines)

print("DONE - found", len(output_lines))