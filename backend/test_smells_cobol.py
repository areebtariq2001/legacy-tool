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
r = main.detect_code_smells(code, "test.cbl")
print(r.get("smell_summary"))
print(r.get("code_smells"))