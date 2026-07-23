import main
code = """PROCEDURE DIVISION.
MAIN-LOGIC.
    IF WS-A
        IF WS-B
            IF WS-C
                DISPLAY "deep"
            END-IF
        END-IF
    END-IF."""
r = main.suggest_refactoring(code, "test.cbl", "cobol")
print(r.get("refactor_summary"))