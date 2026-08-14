import os
os.environ["DATABASE_URL"] = "postgresql://fake:fake@localhost:1/fake"
import main
with open("force_db_test2.txt", "w") as out:
    try:
        result = main._get_db_connection()
        out.write("SUCCESS - result: " + str(result) + " | last_error: " + str(main._LAST_DB_ERROR))
    except Exception as e:
        out.write("CRASHED: " + str(type(e).__name__) + ": " + str(e))
print("DONE genuinely")
