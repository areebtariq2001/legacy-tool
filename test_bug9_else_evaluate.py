import main

test_code = """       PROCEDURE DIVISION.
           EVALUATE WS-X
               WHEN 1
                   IF WS-Y GREATER THAN 5
                       DISPLAY "BIG"
                   ELSE
                       DISPLAY "SMALL"
                   END-IF
               WHEN OTHER
                   DISPLAY "OTHER"
           END-EVALUATE.
           STOP RUN."""

result = main.migrate_cobol(test_code)
with open("bug9_test_output.txt", "w", encoding="utf-8") as f:
    f.write(result["migrated_code"])
print("=== Genuinely-valid-Python check ===")
try:
    compile(result["migrated_code"], "<test>", "exec")
    print("VALID PYTHON")
except SyntaxError as e:
    print("SYNTAX ERROR:", e)