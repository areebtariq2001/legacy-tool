import main
import ast as stdlib_ast

with open("zzz_ast_output.txt", "w") as f:
    f.write("main.ast is stdlib ast: " + str(main.ast is stdlib_ast) + "\n")
    f.write("main.ast: " + str(main.ast) + "\n")
    f.write("main.ast.FunctionDef: " + str(main.ast.FunctionDef) + "\n")
    f.write("stdlib FunctionDef: " + str(stdlib_ast.FunctionDef) + "\n")
    f.write("Same class: " + str(main.ast.FunctionDef is stdlib_ast.FunctionDef) + "\n")

print("DONE")