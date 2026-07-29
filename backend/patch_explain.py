with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    prompt = f"You are a programming teacher. Explain this {language} code in simple terms, section by section, so a beginner can understand what it does. IMPORTANT: When mentioning function or variable names, wrap them in backticks (like `function_name`) so underscores render correctly and are not mistaken for markdown formatting:\\n\\n{source}"'''

new = '''    prompt = f"You are a senior software engineer and security reviewer explaining {language} code to another developer. Explain the code in simple terms, section by section, so a beginner can understand what it does. IMPORTANT: When mentioning function or variable names, wrap them in backticks (like `function_name`) so underscores render correctly and are not mistaken for markdown formatting. If you notice a genuine security or compliance risk in the code (such as hardcoded credentials, SQL injection risk, weak cryptography, or command injection), add a short 'Risk Notes' section at the end covering, for each risk found: Why it is dangerous, likely Impact if exploited, and a brief suggested fix direction (do not invent specific OWASP numbers unless you are certain they are correct - it is fine to describe the risk category in plain English instead, e.g. 'this is a form of injection risk' rather than citing a specific unverified reference number). Only include the Risk Notes section if there is a genuine risk in the code - do not fabricate risks that are not present:\\n\\n{source}"'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")