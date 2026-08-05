import main
import inspect

src = inspect.getsource(main.get_audit_log_json)
with open("audit_log_json_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")