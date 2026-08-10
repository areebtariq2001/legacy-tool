import ast

source = '''def calculate_interest(balance):
    return balance * 0.05

def fraud_score(txn):
    check = lambda x: calculate_interest(x)
    return check(txn)'''

tree = ast.parse(source)
defined_functions = []
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        defined_functions.append(node.name)

calls_map = {}
for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        inner_calls = []
        for sub in ast.walk(node):
            if isinstance(sub, ast.Call):
                fname = None
                if isinstance(sub.func, ast.Name):
                    fname = sub.func.id
                elif isinstance(sub.func, ast.Attribute):
                    fname = sub.func.attr
                if fname and fname in defined_functions and fname != node.name:
                    if fname not in inner_calls:
                        inner_calls.append(fname)
        calls_map[node.name] = inner_calls

with open("zzz_debug99_output.txt", "w") as f:
    f.write(str(calls_map))
print("ZZZ SCRIPT GENUINELY DONE")