import main

with open("testusagelog_result.txt", "w", encoding="utf-8") as out:
    try:
        main.write_audit_log("test-usage-log-table-creation", "test.py", "verifying table creation works", user_email="verify@test.com", ip="9.9.9.9")
        out.write("Genuinely-write_audit_log-call-completed-without-exception\n\n")

        # Now query the DB directly to confirm the table exists and has our row
        conn = main._get_db_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("SELECT action, filename, user_email, ip FROM usage_log WHERE action = %s ORDER BY id DESC LIMIT 1", ("test-usage-log-table-creation",))
            row = cur.fetchone()
            cur.close()
            conn.close()
            out.write("Genuinely-row-found-in-usage_log: " + str(row is not None) + chr(10))
            out.write("Genuinely-row-content: " + str(row))
        else:
            out.write("Genuinely-no-DB-connection-available")
    except Exception as e:
        out.write("Genuinely-FAILED-with-exception: " + str(e))
print("TESTUSAGELOG-DONE")