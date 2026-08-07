with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

with open("extract_aml_endpoint_output.txt", "w", encoding="utf-8") as out:
    for i in range(2352, 2366):
        out.write(str(i + 1) + ": " + lines[i])

print("DONE")