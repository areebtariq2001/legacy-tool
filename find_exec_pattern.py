with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("exec_pattern_output.txt", "w", encoding="utf-8") as out:
    if "'exec '" in content:
        idx = content.find("'exec '")
        out.write("FOUND 'exec ' at char " + str(idx) + "\n")
        out.write(content[max(0,idx-100):idx+150])
    else:
        out.write("Pattern 'exec ' not found literally\n")

print("DONE")