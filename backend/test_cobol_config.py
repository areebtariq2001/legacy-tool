import main
code = """01 DB-HOST PIC X(20) VALUE "mainframe.local".
01 DB-USER PIC X(20) VALUE "SYSADMIN".
01 DB-PASSWORD PIC X(20) VALUE "Cobol1985Pass"."""
r = main.suggest_config_migration(code, "test.cbl")
print(r.get("config_summary"))