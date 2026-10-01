import main

with open("testthese3v2_result.txt", "w", encoding="utf-8") as out:
    # Test 1: has_key with dotted path via the real migrate_code function
    test_code = "if self.cache.has_key(k):\n    pass"
    result1 = main.migrate_code(test_code)
    out.write("Test-1 (has_key-dotted-path): migrated_code=" + chr(10) + result1["migrated_code"] + chr(10))
    out.write("(expect 'if k in self.cache:' - the 'self.' prefix should be preserved)" + chr(10) + chr(10))

    # Test 2: jailbreak false-positive fixed
    fp_test = main._check_jailbreak_output("The analysis shows this code checks if the device is jailbroken before allowing access.")
    out.write("Test-2 (jailbroken-false-positive): blocked=" + str(fp_test) + " (expect False now)" + chr(10) + chr(10))

    # Test 3: GitHub owner/repo ".." rejection
    result3 = main.fetch_github_issues("https://github.com/owner../repo")
    out.write("Test-3 (dotdot-in-owner-rejected): " + str(result3.get("error", "NO-ERROR-RETURNED")) + " (expect an Invalid-owner error)")
print("TESTTHESE3V2-DONE")