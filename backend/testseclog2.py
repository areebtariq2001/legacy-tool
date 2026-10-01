import main

for i in range(250):
    main._record_security_event("test_event", "1.2.3." + str(i % 255), "test detail " + str(i))

is_valid1, reason1 = main._verify_security_log_integrity()

# Now genuinely tamper with one entry and confirm it's STILL detected
main._security_log[50]["detail"] = "TAMPERED-VALUE"
is_valid2, reason2 = main._verify_security_log_integrity()

with open("testseclog2_result.txt", "w", encoding="utf-8") as out:
    out.write("Test-1 (250-normal-events, no-tampering): is_valid=" + str(is_valid1) + " (expect True now)" + chr(10))
    out.write("reason: " + str(reason1) + chr(10) + chr(10))
    out.write("Test-2 (after-genuine-tampering): is_valid=" + str(is_valid2) + " (expect False - tampering must still be caught)" + chr(10))
    out.write("reason: " + str(reason2))
print("TESTSECLOG2-DONE")