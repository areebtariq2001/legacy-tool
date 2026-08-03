import main

test_code = """       PROCEDURE DIVISION.
           OPEN INPUT FILE-A.
           READ FILE-A.
           WRITE RECORD-A.
           CLOSE FILE-A.
           STOP RUN."""

result = main.migrate_cobol(test_code)
for c in result["changes"]:
    if "REVIEW NEEDED" in c:
        print(c)