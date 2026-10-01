import main

with open("testsplitcommentfinal_result.txt", "w", encoding="utf-8") as out:
    # Test module-level function directly
    before, after = main._split_inline_comment('x = 5  # this is a comment')
    out.write("Test-1 (direct-function-call): before=" + repr(before) + " after=" + repr(after) + chr(10) + chr(10))

    # Test migrate_code (Python)
    py_code = "print 'hello'  # old style print"
    result1 = main.migrate_code(py_code)
    out.write("Test-2 (migrate_code-Python): SUCCEEDED, migrated=" + repr(result1.get("migrated_code", ""))[:100] + chr(10) + chr(10))

    # Test migrate_java
    java_code = "System.out.println(\"hello\");  // test comment"
    result2 = main.migrate_java(java_code)
    out.write("Test-3 (migrate_java): SUCCEEDED, keys=" + str(list(result2.keys())[:5]) + chr(10) + chr(10))

    # Test migrate_php
    php_code = "<?php echo 'hello'; // test comment ?>"
    result3 = main.migrate_php(php_code)
    out.write("Test-4 (migrate_php): SUCCEEDED, keys=" + str(list(result3.keys())[:5]))
print("TESTSPLITCOMMENTFINAL-DONE")