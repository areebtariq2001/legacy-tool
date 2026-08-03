import main

test_code = """       PROCEDURE DIVISION.
           DISPLAY "HELLO".
           END-IF.
           STOP RUN."""

result = main.migrate_cobol(test_code)
for c in result["changes"]:
    if "REVIEW NEEDED" in c:
        print(c)