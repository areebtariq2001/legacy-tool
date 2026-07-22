import main
code = """PROCEDURE DIVISION.
MAIN-LOGIC.
    COMPUTE WS-TOTAL = WS-A + WS-B.
    ADD 100 TO WS-BALANCE.
    SUBTRACT 50 FROM WS-BALANCE.
    PERFORM LOOP-PARA UNTIL WS-DONE = 1.
    STOP RUN."""
r = main.migrate_cobol(code)
print(r.get("changes"))
print("---")
print(r.get("migrated_code"))