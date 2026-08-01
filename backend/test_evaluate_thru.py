import main

test_code = """       IDENTIFICATION DIVISION.
       PROCEDURE DIVISION.
           EVALUATE WS-SCORE
               WHEN 1 THRU 10
                   DISPLAY "LOW"
               WHEN OTHER
                   DISPLAY "HIGH"
           END-EVALUATE.
           STOP RUN."""

result = main.migrate_cobol(test_code)
print("Migrated code:")
print(result["migrated_code"])
print()
print("Genuinely-valid-Python syntax check:")
try:
    compile(result["migrated_code"], "<test>", "exec")
    print("VALID")
except SyntaxError as e:
    print("SYNTAX ERROR:", e)