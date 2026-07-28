import main
code = "IF WS-AMOUNT > WS-DAILY-LIMIT\n    DISPLAY \"BLOCKED - EXCEEDS DAILY LIMIT\"\nEND-IF."
r = main.migrate_cobol(code)
print(r.get("migrated_code"))