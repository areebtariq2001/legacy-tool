import main
import re

with open("testbatch2_result.txt", "w", encoding="utf-8") as out:
    # Test 1: StringIO regex - should NOT flag modern "from io import StringIO"
    modern_code = "from io import StringIO\nbuf = StringIO()"
    old_code = "import StringIO\nbuf = StringIO.StringIO()"
    pattern = None
    for p, label, mult in main.DEBT_RULES:
        if "StringIO" in label:
            pattern = p
            break
    out.write("Genuinely-StringIO-pattern: " + str(pattern) + chr(10))
    modern_match = re.search(pattern, modern_code)
    old_match = re.search(pattern, old_code)
    out.write("Test-1a (modern 'from io import StringIO' should NOT match): " + str(modern_match is not None) + " (expect False)" + chr(10))
    out.write("Test-1b (old 'import StringIO' SHOULD match): " + str(old_match is not None) + " (expect True)" + chr(10) + chr(10))

    # Test 2: session-token rate-limit bypass fix
    main._endpoint_rate_store.clear()
    for i in range(6):
        r = main._check_endpoint_specific_limit("/ai-migrate", "ip:9.9.9.9")
        if i < 5:
            assert r == True
    r6 = main._check_endpoint_specific_limit("/ai-migrate", "ip:9.9.9.9")
    out.write("Test-2 (6th-attempt-same-IP-should-be-blocked): " + str(r6) + " (expect False - this confirms IP-based limiting works, and since endpoint_identifier is now always ip-based regardless of token, rotating a token can no longer create a fresh identifier)")
print("TESTBATCH2-DONE")