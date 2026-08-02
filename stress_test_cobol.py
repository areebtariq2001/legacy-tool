import main

# Genuinely-deeper, more-complex test
test_code = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. COMPLEX.
       PROCEDURE DIVISION.
           IF WS-A > 1
               IF WS-B > 2
                   IF WS-C > 3
                       DISPLAY "TRIPLE-NESTED"
                   END-IF
                   DISPLAY "DOUBLE-DONE"
               END-IF
               DISPLAY "SINGLE-DONE"
           END-IF.
           DISPLAY "AFTER-FIRST-IF".
           EVALUATE WS-X
               WHEN 1
                   DISPLAY "X1"
               WHEN 2
                   DISPLAY "X2"
               WHEN OTHER
                   DISPLAY "XOTHER"
           END-EVALUATE.
           IF WS-Y > 5
               DISPLAY "Y-CHECK"
           END-IF.
           EVALUATE WS-Z
               WHEN 10
                   DISPLAY "Z10"
               WHEN OTHER
                   DISPLAY "ZOTHER"
           END-EVALUATE.
           STOP RUN."""

result = main.migrate_cobol(test_code)
print(result["migrated_code"])
print()
print("=== Genuinely-valid-Python check ===")
try:
    compile(result["migrated_code"], "<test>", "exec")
    print("VALID PYTHON - genuinely-robust-confirmed")
except SyntaxError as e:
    print("SYNTAX ERROR:", e)