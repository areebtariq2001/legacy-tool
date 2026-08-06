import main
import inspect

src = inspect.getsource(main.scan_sql_injection)
with open("scan_sqli_checks.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")