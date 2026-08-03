import main

test_code = """       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 WS-RECORD.
       05 WS-NAME PIC X(30).
       05 WS-AGE PIC 9(3) VALUE ZEROS.
       PROCEDURE DIVISION.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("level_test_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")