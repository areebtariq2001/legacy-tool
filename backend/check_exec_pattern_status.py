with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("exec_status_output.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely still has 'exec ' loose pattern: " + str("'exec '" in content) + "\n")

print("DONE")