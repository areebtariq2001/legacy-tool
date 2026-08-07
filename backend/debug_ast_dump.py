import ast

with open("PASTE_YOUR_TEST_FILE_PATH_HERE.py", "r", encoding="utf-8") as f:
    source = f.read()

tree = ast.parse(source)
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef) and node.name == "fraud_score":
        with open("fraud_score_ast_dump.txt", "w", encoding="utf-8") as out:
            out.write(ast.dump(node, indent=2))
        print("DONE - dumped fraud_score AST")