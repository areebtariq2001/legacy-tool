with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''        f"ORIGINAL:\\n{original}\\n\\nMIGRATED:\\n{migrated}"
    )
    response = call_groq(prompt, max_tokens=300)'''

new = '''        f"ORIGINAL:\\n{original}\\n\\nMIGRATED:\\n{migrated}"
    )
    response = call_ai_provider(prompt, max_tokens=300)'''

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")