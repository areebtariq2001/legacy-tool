import main

with open("testpoolnodb_result.txt", "w", encoding="utf-8") as out:
    conn = main._get_db_connection()
    out.write("Genuinely-conn-is-None (expect True, since no DATABASE_URL): " + str(conn is None) + chr(10))
    out.write("Genuinely-_LAST_DB_ERROR: " + str(main._LAST_DB_ERROR) + chr(10) + chr(10))

    # Also test calling it multiple times to confirm consistent behavior
    conn2 = main._get_db_connection()
    out.write("Genuinely-2nd-call-also-None: " + str(conn2 is None))
print("TESTPOOLNODB-DONE")