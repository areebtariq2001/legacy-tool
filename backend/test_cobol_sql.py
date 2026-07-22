import main
code = """EXEC SQL
    SELECT BALANCE INTO :WS-BALANCE
    FROM ACCOUNTS
    WHERE ACCOUNT_ID = 'ACCT-ID-VALUE'
END-EXEC."""
r = main.scan_sql_injection(code, "test.cbl")
print(r.get("sqli_summary"))
print(r.get("sqli_issues"))