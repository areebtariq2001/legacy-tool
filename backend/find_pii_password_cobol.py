with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

count = content.count("Hardcoded password (COBOL VALUE clause)")
with open("pii_password_cobol_output.txt", "w", encoding="utf-8") as out:
    out.write("Count: " + str(count) + "\n")
    idx = 0
    for i in range(count):
        idx = content.find("Hardcoded password (COBOL VALUE clause)", idx)
        out.write("Found at position: " + str(idx) + "\n")
        out.write(content[max(0,idx-200):idx+50] + "\n---\n")
        idx += 1

print("DONE")