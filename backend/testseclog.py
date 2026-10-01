import main

for i in range(250):
    main._record_security_event("test_event", "1.2.3." + str(i % 255), "test detail " + str(i))

is_valid, reason = main._verify_security_log_integrity()

with open("testseclog_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-total-events-recorded: 250" + chr(10))
    out.write("Genuinely-log-length-after-truncation: " + str(len(main._security_log)) + " (expect capped at 200)" + chr(10))
    out.write("Genuinely-is_valid: " + str(is_valid) + " (this is the KEY question - is it falsely False?)" + chr(10))
    out.write("Genuinely-reason: " + str(reason))
print("TESTSECLOG-DONE")