import main
import re

with open("testthese3_result.txt", "w", encoding="utf-8") as out:
    # Test 1: has_key with dotted path
    test_line = "if self.cache.has_key(k):"
    result = re.sub(r'((?:\w+\.)*\w+)\.has_key\(([^)]+)\)', main._safe_haskey_sub, test_line)
    out.write("Test-1 (has_key-dotted-path): '" + test_line + "' -> '" + result + "' (expect 'if k in self.cache:')" + chr(10) + chr(10))

    # Test 2: jailbreak false-positive fixed
    fp_test = main._check_jailbreak_output("The analysis shows this code checks if the device is jailbroken before allowing access.")
    out.write("Test-2 (jailbroken-false-positive): blocked=" + str(fp_test) + " (expect False now)" + chr(10) + chr(10))

    # Test 3: GitHub owner/repo ".." rejection
    result3 = main.fetch_github_issues("https://github.com/owner../repo")
    out.write("Test-3 (dotdot-in-owner-rejected): " + str(result3.get("error", "NO-ERROR-RETURNED")) + " (expect an Invalid-owner error)")
print("TESTTHESE3-DONE")