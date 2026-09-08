with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()
count = content.count("ast.parse(")
with open("ast_parse_count_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-total-ast.parse-calls-in-codebase: " + str(count))
print("AST-PARSE-COUNT-DONE")