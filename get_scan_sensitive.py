import main
import inspect

src1 = inspect.getsource(main.scan_sensitive_data)
with open("scan_sensitive_full.txt", "w", encoding="utf-8") as out:
    out.write(src1)

print("DONE - length:", len(src1))