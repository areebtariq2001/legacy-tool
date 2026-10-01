import main

with open("testjavastringliteral_result.txt", "w", encoding="utf-8") as out:
    # Test 1: EXACT advisor scenario - string literal should NOT be rewritten
    test1_code = 'String msg = "Use new Integer(5) instead of autoboxing";'
    result1 = main.migrate_java(test1_code)
    out.write("Test-1 (string-literal-should-NOT-be-rewritten):\n")
    out.write("Genuinely-migrated_code: " + result1["migrated_code"] + chr(10))
    out.write("Genuinely-string-preserved-correctly: " + str('new Integer(5)' in result1["migrated_code"]) + " (expect True)" + chr(10) + chr(10))

    # Test 2: genuine case should STILL be rewritten (real code, not a string)
    test2_code = 'Integer x = new Integer(5);'
    result2 = main.migrate_java(test2_code)
    out.write("Test-2 (genuine-new-Integer-should-still-be-rewritten):\n")
    out.write("Genuinely-migrated_code: " + result2["migrated_code"] + chr(10))
    out.write("Genuinely-correctly-rewritten: " + str('Integer.valueOf(5)' in result2["migrated_code"]) + " (expect True)" + chr(10) + chr(10))

    # Test 3: EXACT advisor scenario 2 - comment should NOT trigger review warning
    test3_code = 'StringBuilder sb = new StringBuilder();\nsb.append(x); // was StringBuffer before refactor'
    result3 = main.migrate_java(test3_code)
    out.write("Test-3 (comment-mentioning-StringBuffer-should-NOT-trigger-warning):\n")
    out.write("Genuinely-changes: " + str(result3["changes"]) + chr(10))
    out.write("Genuinely-falsely-triggered: " + str(any("StringBuffer" in c for c in result3["changes"])) + " (expect False)" + chr(10) + chr(10))

    # Test 4: genuine StringBuffer usage should STILL trigger the review warning
    test4_code = 'StringBuffer sb = new StringBuffer();\nsb.append(x);'
    result4 = main.migrate_java(test4_code)
    out.write("Test-4 (genuine-StringBuffer-usage-should-still-trigger-warning):\n")
    out.write("Genuinely-changes: " + str(result4["changes"]) + chr(10))
    out.write("Genuinely-correctly-triggered: " + str(any("StringBuffer" in c for c in result4["changes"])) + " (expect True)")
print("TESTJAVASTRINGLITERAL-DONE")