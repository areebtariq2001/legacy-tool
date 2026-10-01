import main

with open("testneverlog_result.txt", "w", encoding="utf-8") as out:
    # Test 1: DB connection string with embedded credentials
    test1 = "Connection failed: postgresql://myuser:supersecret123@aws-pooler.example.com:6543/postgres"
    result1 = main.safe_log_message(test1)
    out.write("Test-1 (DB-URL-redaction): " + result1 + chr(10))
    out.write("Genuinely-password-redacted: " + str("supersecret123" not in result1) + " (expect True)" + chr(10) + chr(10))

    # Test 2: Bearer token
    test2 = "Request failed with header Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.abc123xyz"
    result2 = main.safe_log_message(test2)
    out.write("Test-2 (Bearer-token-redaction): " + result2 + chr(10))
    out.write("Genuinely-token-redacted: " + str("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9" not in result2) + " (expect True)")
print("TESTNEVERLOG-DONE")