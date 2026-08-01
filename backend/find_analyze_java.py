import main
import inspect

java_src = inspect.getsource(main.analyze_java)
cobol_src = inspect.getsource(main.analyze_cobol)

with open("lang_check_output.txt", "w", encoding="utf-8") as out:
    out.write("=== analyze_java ===\n")
    out.write("Has scan_sql_injection: " + str("scan_sql_injection" in java_src) + "\n")
    out.write("Has password-regex: " + str("password" in java_src.lower()) + "\n")
    out.write("\n=== analyze_cobol ===\n")
    out.write("Has scan_sql_injection: " + str("scan_sql_injection" in cobol_src) + "\n")
    out.write("Has password-regex: " + str("password" in cobol_src.lower()) + "\n")

print("DONE")