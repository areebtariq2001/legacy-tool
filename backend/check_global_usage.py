with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("global_usage_output.txt", "w", encoding="utf-8") as out:
    out.write("_seqre total count in whole file: " + str(content.count("_seqre")) + "\n")
    out.write("_mre total count in whole file: " + str(content.count("_mre")) + "\n")

print("DONE")