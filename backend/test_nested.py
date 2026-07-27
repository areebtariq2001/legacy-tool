import main
code = "IF WS-A = 1\n    ADD 100 TO WS-BALANCE\n    SUBTRACT 50 FROM WS-BALANCE\nEND-IF."
r = main.migrate_cobol(code)
print(r.get("migrated_code"))