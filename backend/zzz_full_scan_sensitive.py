import main
import inspect

src = inspect.getsource(main.scan_sensitive_data)
with open("zzz_scan_sensitive_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))