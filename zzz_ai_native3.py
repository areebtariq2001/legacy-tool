import main
import inspect

src = inspect.getsource(main.check_ai_native_readiness)
with open("zzz_ai_native3_out.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))