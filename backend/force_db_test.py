import os
os.environ["DATABASE_URL"] = "postgresql://fake:fake@localhost:1/fake"
import main
with open("force_db_test.txt", "w") as out:
    try:
        result = main._get_db_connection()
        out.write("SUCCESS - no NameError, result: " + str(result) + " | last_error: " + str(main._LAST_DB_ERROR))
    except NameError as e:
        out.write("CRITICAL NameError: " + str(e))
    except Exception as e:
        out.write("Other exception (genuinely expected, connection refused): " + str(type(e).__name__) + ": " + str(e)[:200])
print("DONE genuinely")
