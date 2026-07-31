import main

code = "def foo(x, y):\n    z = True\n    print(len(x))\n    return z + y"
result = main.extract_variables(code)
print("Extracted:", sorted(result))
print("'True' in result:", "True" in result)
print("'print' in result:", "print" in result)
print("'len' in result:", "len" in result)
print("'x' in result:", "x" in result)
print("'z' in result:", "z" in result)