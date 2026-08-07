import main
import inspect

src = inspect.getsource(main.analyze_cobol)
with open("cobol_calls_check.txt", "w", encoding="utf-8") as out:
    out.write("Calls scan_sensitive_data: " + str("scan_sensitive_data" in src) + "\n")
    out.write("Calls scan_sql_injection: " + str("scan_sql_injection" in src) + "\n")

print("DONE")