import main

comment_test = '<?php\n// password = "change_me"\n?>'
result1 = main.analyze_php(comment_test)
print("Comment-only test - issues:", result1["issues"])

genuine_test = '<?php\n$password = "actualSecret123";\n?>'
result2 = main.analyze_php(genuine_test)
print("Genuine-hardcoded test - issues:", result2["issues"])