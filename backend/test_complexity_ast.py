import main

# Genuine Python code with real complexity
python_code = """
def simple_func(x):
    return x + 1

def complex_func(a, b, c):
    if a:
        for i in range(10):
            if b and c:
                while i < 5:
                    if a or b:
                        pass
    return a
"""
result1 = main.calculate_complexity(python_code)
print("Python (AST-based):", result1)

# Non-Python code (should fall back to heuristic)
php_code = """
function old_style_array() {
    $arr = array("a" => 1, "b" => 2);
    if ($arr) {
        return each($arr);
    }
}
"""
result2 = main.calculate_complexity(php_code)
print("PHP (heuristic fallback):", result2)