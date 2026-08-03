import main

test_code = """       PROCEDURE DIVISION.
           MOVE WS-SOURCE TO WS-DEST.
           MOVE A TO B C D.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("move_multi_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("DONE")