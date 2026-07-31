import main

# Case 1: The problematic case - unbalanced brace inside string
test1 = '<?php\nfunction test() {\n    $msg = "Cost: {";\n    return $msg;\n}'
result1 = main.validate_php(test1)
print("Test 1 (brace in string):", result1["valid"], "-", result1["validation_message"][:80])

# Case 2: Genuinely broken PHP (real mismatched brace)
test2 = '<?php\nfunction test() {\n    return true;'
result2 = main.validate_php(test2)
print("Test 2 (genuinely broken):", result2["valid"], "-", result2["validation_message"][:80])

# Case 3: Valid normal PHP
test3 = '<?php\nfunction test() {\n    return true;\n}'
result3 = main.validate_php(test3)
print("Test 3 (valid normal):", result3["valid"])