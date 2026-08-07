import main
import inspect

src = inspect.getsource(main.analyze_cobol)
idx = src.find("scan_sql_injection")
with open("cobol_sqli_part.txt", "w", encoding="utf-8") as out:
    out.write(src[max(0,idx-100):idx+400])

print("DONE")