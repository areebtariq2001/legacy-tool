import main

with open("testcritical2_result.txt", "w", encoding="utf-8") as out:
    # Test 1: urllib.parse works now
    try:
        result = main.urllib.parse.urlparse("https://raw.githubusercontent.com/test/path")
        out.write("Genuinely-urllib.parse-works: True, hostname=" + result.hostname + chr(10))
    except Exception as e:
        out.write("Genuinely-urllib.parse-FAILED: " + str(e) + chr(10))

    # Test 2: endpoint limit now correctly applies to /auth/login
    out.write(chr(10) + "Genuinely-ENDPOINT_LIMITS: " + str(main._ENDPOINT_SPECIFIC_LIMITS) + chr(10))
    test_id = "test-ip-endpoint-check"
    main._endpoint_rate_store.pop("/auth/login|" + test_id, None)
    results_list = []
    for i in range(7):
        r = main._check_endpoint_specific_limit("/auth/login", test_id)
        results_list.append(r)
    out.write("Genuinely-7-attempts-on-/auth/login (limit=5): " + str(results_list) + chr(10))
    out.write("Genuinely-blocked-after-5 (should have False in there): " + str(False in results_list))
print("TESTCRITICAL2-DONE")