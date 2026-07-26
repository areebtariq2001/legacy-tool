import main
code = "IF WS-A = 1\n    DISPLAY 1\nELSE\n    DISPLAY 2\nEND-IF."
r = main.migrate_cobol(code)
print(r.get("migrated_code"))