import main
import inspect

funcs_to_check = ["migrate_code", "extract_variables", "check_variable_integrity", "calculate_complexity", "deep_verify_python"]

with open("other_ast_functions_check.txt", "w", encoding="utf-8") as out:
    for fname in funcs_to_check:
        func = getattr(main, fname)
        src = inspect.getsource(func)
        has_ast_parse = "ast.parse" in src
        has_early_empty_return = "except:" in src and "return" in src.split("except:")[1].split("\n")[1] if "except:" in src else False
        out.write(f"{fname}: has_ast.parse={has_ast_parse}\n")

print("DONE")