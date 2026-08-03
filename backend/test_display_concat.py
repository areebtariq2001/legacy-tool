import main

test_code = """       PROCEDURE DIVISION.
           DISPLAY "Hello " WS-NAME "!".
           DISPLAY "Insufficient balance".
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("display_test_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")