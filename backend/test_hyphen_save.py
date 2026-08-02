import main

test_code = """       PROCEDURE DIVISION.
           COMPUTE RESULT = A - B.
           ADD -5 TO COUNTER.
           SUBTRACT -5 FROM TOTAL.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("hyphen_test_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")