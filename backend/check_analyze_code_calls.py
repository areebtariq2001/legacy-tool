import main
import inspect

src = inspect.getsource(main.analyze_code)
with open("analyze_code_calls_check.txt", "w", encoding="utf-8") as out:
    out.write("Calls scan_sql_injection: " + str("scan_sql_injection" in src) + "\n")
    out.write("Calls scan_sensitive_data: " + str("scan_sensitive_data" in src) + "\n")
    out.write("\n=== FULL SOURCE ===\n")
    out.write(src)

print("DONE")