import main

# Simulate a "big file, many simple functions" scenario
simple_multi_func = "\n".join([f"def func{i}():\n    return {i}" for i in range(20)])
result1 = main.calculate_complexity(simple_multi_func)
print("20 simple functions:", result1)

# A single genuinely complex function
complex_single = """
def complex_func(a, b, c):
    if a:
        for i in range(10):
            if b and c:
                while i < 5:
                    if a or b:
                        pass
"""
result2 = main.calculate_complexity(complex_single)
print("1 genuinely complex function:", result2)