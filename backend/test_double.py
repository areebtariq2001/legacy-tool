import main
code = "IF WS-A = 1\n    IF WS-B = 2\n        DISPLAY 1\n    END-IF\nEND-IF."
r = main.migrate_cobol(code)
print(r.get("migrated_code"))