import main

test_code = """       PROCEDURE DIVISION.
           COMPUTE RESULT = A - B.
           ADD -5 TO COUNTER.
           SUBTRACT -5 FROM TOTAL.
           STOP RUN."""

result = main.migrate_cobol(test_code)
print(result["migrated_code"])