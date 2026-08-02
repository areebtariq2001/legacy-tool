import main

test_code = """       PROCEDURE DIVISION.
           PERFORM LOOP-PARA UNTIL WS-COUNT > 10.
           PERFORM CHECK-PARA UNTIL COUNT EQUAL ZERO.
           PERFORM NAME-PARA UNTIL WS-NAME EQUAL SPACES.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("perform_operators_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")