import main
code = "EVALUATE WS-STATUS\n    WHEN 1\n        DISPLAY 1\n    WHEN 2\n        DISPLAY 2\n    WHEN OTHER\n        DISPLAY 0\nEND-EVALUATE."
r = main.migrate_cobol(code)
print(r.get("migrated_code"))