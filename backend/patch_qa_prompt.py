with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

old = '''    prompt = ("You are a senior developer helping someone understand a legacy codebase. "
              "Based ONLY on the code below, answer the question clearly and concisely in plain English. "
              "If the code does not contain enough information to answer, say so honestly. "
              "IMPORTANT: Only describe functionality that is ACTUALLY implemented in the code. Do not infer behavior from function/variable names alone (e.g. a function named 'log' or 'buildLog' that only returns a string, without any file-write or logging-library call, does NOT have a real logging mechanism - describe only what the code literally does).\\n\\n"
              "CODE:\\n" + source[:6000] + "\\n\\n"
              "QUESTION: " + question + "\\n\\n"
              "ANSWER:")'''

new = '''    numbered_source = chr(10).join(str(i + 1) + ": " + ln for i, ln in enumerate(source.split(chr(10))))
    prompt = ("You are a senior developer helping someone understand a legacy codebase. "
              "The code below has line numbers prefixed (e.g. '12: some code'). "
              "Based ONLY on the code below, answer the question clearly and concisely in plain English. "
              "IMPORTANT: When you reference a specific function, variable, or behavior, cite the line number(s) it appears on, e.g. 'the calculate_interest() function (line 4) does X'. "
              "If the code does not contain enough information to answer, say so honestly. "
              "IMPORTANT: Only describe functionality that is ACTUALLY implemented in the code. Do not infer behavior from function/variable names alone (e.g. a function named 'log' or 'buildLog' that only returns a string, without any file-write or logging-library call, does NOT have a real logging mechanism - describe only what the code literally does).\\n\\n"
              "CODE (with line numbers):\\n" + numbered_source[:6500] + "\\n\\n"
              "QUESTION: " + question + "\\n\\n"
              "ANSWER (cite line numbers for every function or behavior you mention):")'''

count = content.count(old)
print("Occurrences found:", count)

if count == 1:
    content = content.replace(old, new, 1)
    with open("main.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("PATCHED SUCCESSFULLY")
else:
    print("FAILED - aborting to be safe")