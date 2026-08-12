import main
import inspect

src = inspect.getsource(main.detect_fraud_gaps)
with open("zzz_fraud_gaps_out.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))