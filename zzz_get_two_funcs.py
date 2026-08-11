import main
import inspect

src1 = inspect.getsource(main.extract_business_rules)
src2 = inspect.getsource(main.check_ai_native_readiness)

with open("zzz_extract_rules.txt", "w", encoding="utf-8") as out:
    out.write(src1)

with open("zzz_ai_native.txt", "w", encoding="utf-8") as out2:
    out2.write(src2)

print("DONE - extract:", len(src1), "ai_native:", len(src2))