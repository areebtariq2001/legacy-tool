with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
count = content.count("Could not parse file (non-Python-3 syntax).")
with open("count_parse_error_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-total-occurrences: " + str(count))
print("COUNT-PARSE-ERROR-DONE")