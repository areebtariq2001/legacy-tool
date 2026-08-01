import main

test_code = """       IDENTIFICATION DIVISION.
       PROCEDURE DIVISION.
           MOVE WS-SOURCE TO WS-DEST.
           MOVE "HELLO" TO WS-GREETING.
           MOVE 0 TO WS-COUNTER.
           STOP RUN."""

result = main.migrate_cobol(test_code)
print("Changes:")
for c in result["changes"]:
    print(" -", c[:90])