import main

# Test normal PHP migration still works
normal_php = b'<?php\nfunction test() {\n    return true;\n}\n?>'
result1 = main.safe_read_file(normal_php, "test.php")
print("Normal PHP - source returned:", result1[0] is not None, "- error:", result1[1])

# Test empty file genuinely rejected
empty_bytes = b''
result2 = main.safe_read_file(empty_bytes, "test.php")
print("Empty PHP - source returned:", result2[0], "- error:", result2[1])

# Test genuinely oversized (simulate)
huge_bytes = b'x' * (main.MAX_FILE_SIZE + 1000)
result3 = main.safe_read_file(huge_bytes, "test.php")
print("Oversized PHP - source returned:", result3[0], "- error:", result3[1])