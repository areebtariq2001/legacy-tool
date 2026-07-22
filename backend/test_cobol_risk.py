import main
code = """EXEC SQL
    SELECT BALANCE INTO :WS-BALANCE
    FROM ACCOUNTS
    WHERE ACCOUNT_ID = 'ACCT-ID-VALUE'
END-EXEC.
PROCEDURE DIVISION.
MAIN-LOGIC.
    IF WS-IS-FLAGGED
        DISPLAY "BLOCKED"."""
r = main.predict_migration_risk(code, "test.cbl")
print(r)