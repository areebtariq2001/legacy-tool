import main
import inspect

src = inspect.getsource(main.write_audit_log)
with open("write_audit_log_source.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")