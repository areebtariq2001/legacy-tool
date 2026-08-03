import main

test_code = """       PROCEDURE DIVISION.
           IF WS-COUNT GREATER THAN 10
               DISPLAY "BIG"
           END-IF.
           IF WS-NAME EQUAL TO SPACES
               DISPLAY "EMPTY"
           END-IF.
           IF WS-FLAG NOT EQUAL ZERO
               DISPLAY "SET"
           END-IF.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("if_ops_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")