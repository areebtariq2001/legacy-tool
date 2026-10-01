import main

with open("testapproval_result.txt", "w", encoding="utf-8") as out:
    try:
        result = main.save_approval_decision("test.py", "Approved", "looks good", "migration", approved_by="tester@example.com")
        out.write("Test-1 (with-approved_by-param): SUCCEEDED, result=" + str(result) + chr(10))
    except Exception as e:
        out.write("Test-1: FAILED with " + str(e) + chr(10))

    # Backward compat: old-style call without approved_by
    try:
        result2 = main.save_approval_decision("test2.py", "Approved", "ok", "migration")
        out.write("Test-2 (old-style-no-approved_by, backward-compat): SUCCEEDED, result=" + str(result2))
    except Exception as e:
        out.write("Test-2: FAILED with " + str(e))
print("TESTAPPROVAL-DONE")