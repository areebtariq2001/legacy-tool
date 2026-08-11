import main
import inspect

print("Has funcs_has_no_hints:", hasattr(main, 'funcs_has_no_hints'))

src1 = inspect.getsource(main.check_ai_native_readiness)
with open("zzz_ai_native2.txt", "w", encoding="utf-8") as out:
    out.write(src1)

if hasattr(main, 'funcs_has_no_hints'):
    src2 = inspect.getsource(main.funcs_has_no_hints)
    with open("zzz_hints_func.txt", "w", encoding="utf-8") as out2:
        out2.write(src2)

print("DONE")