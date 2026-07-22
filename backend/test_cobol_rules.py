import main
code = """PROCEDURE DIVISION.
MAIN-LOGIC.
    IF WS-IS-FLAGGED
        DISPLAY "BLOCKED".
    IF WS-BALANCE < 0
        DISPLAY "DECLINED".
    IF WS-AMOUNT > WS-DAILY-LIMIT
        DISPLAY "EXCEEDED"."""
r = main.discover_business_rules_engine(code, "test.cbl")
print(r.get("rules_summary"))