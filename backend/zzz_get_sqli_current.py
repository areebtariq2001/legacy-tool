import main
import inspect

src = inspect.getsource(main.scan_sql_injection)
with open("zzz_sqli_current.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))