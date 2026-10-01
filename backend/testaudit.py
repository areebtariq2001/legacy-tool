import main

with open("testaudit_result.txt", "w", encoding="utf-8") as out:
    # Test 1: OLD-style call (backward compat, 3 args only)
    try:
        main.write_audit_log("test-action-old", "test.py", "old-style-call-worked")
        out.write("Test-1 (old-style-3-arg-call): SUCCEEDED (no exception raised)\n")
    except Exception as e:
        out.write("Test-1 (old-style-3-arg-call): FAILED with " + str(e) + "\n")

    latest_block_old = main.audit_blockchain.chain[-1]
    out.write("Genuinely-old-style-block-user_email: " + latest_block_old.user_email + " (expect anonymous)\n\n")

    # Test 2: NEW-style call with real attribution
    main.write_audit_log("test-action-new", "test2.py", "new-style-call-worked", user_email="real@user.com", ip="5.6.7.8")
    latest_block_new = main.audit_blockchain.chain[-1]
    out.write("Genuinely-new-style-block-user_email: " + latest_block_new.user_email + " (expect real@user.com)\n")
    out.write("Genuinely-new-style-block-ip: " + latest_block_new.ip + " (expect 5.6.7.8)")
print("TESTAUDIT-DONE")