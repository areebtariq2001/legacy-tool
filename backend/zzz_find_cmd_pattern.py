import main
import inspect

src = inspect.getsource(main.scan_sensitive_data)
idx = src.lower().find("command")
with open("zzz_cmd_context.txt", "w", encoding="utf-8") as out:
    out.write(src[max(0,idx-200):idx+300])

print("DONE")