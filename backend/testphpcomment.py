import main

with open("testphpcomment_result.txt", "w", encoding="utf-8") as out:
    # Test 1: comment mentioning "split(" should NOT trigger review warning
    test1_code = '<?php\n$x = 5; // used to use split( here before refactor\n?>'
    result1 = main.migrate_php(test1_code)
    out.write("Test-1 (comment-mentioning-split-should-NOT-trigger): changes=" + str(result1["changes"]) + chr(10))
    out.write("Genuinely-falsely-triggered: " + str(any("split()" in c for c in result1["changes"])) + " (expect False)" + chr(10) + chr(10))

    # Test 2: genuine split( usage should STILL trigger
    test2_code = '<?php\n$parts = split("/", $path);\n?>'
    result2 = main.migrate_php(test2_code)
    out.write("Test-2 (genuine-split-usage-should-still-trigger): changes=" + str(result2["changes"]) + chr(10))
    out.write("Genuinely-correctly-triggered: " + str(any("split()" in c for c in result2["changes"])) + " (expect True)")
print("TESTPHPCOMMENT-DONE")