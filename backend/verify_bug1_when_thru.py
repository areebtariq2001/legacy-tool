import main

test_code = """       PROCEDURE DIVISION.
           EVALUATE WS-SCORE
               WHEN 90 THRU 100
                   MOVE "A" TO WS-GRADE
               WHEN 80 THRU 89
                   MOVE "B" TO WS-GRADE
           END-EVALUATE.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("when_thru_verify.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")