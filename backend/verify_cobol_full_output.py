import main

test_code = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. PAYROLL.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-NAME PIC X(30).
       01 WS-SALARY PIC 9(7) VALUE 5000.
       PROCEDURE DIVISION.
           IF WS-SALARY > 1000
               DISPLAY "HIGH"
               IF WS-NAME = "TEST"
                   DISPLAY "NESTED"
               END-IF
           END-IF.
           EVALUATE WS-SALARY
               WHEN 1
                   DISPLAY "ONE"
               WHEN OTHER
                   DISPLAY "OTHER"
           END-EVALUATE.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("cobol_full_migrated_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")