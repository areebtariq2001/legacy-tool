import main
import inspect

src = inspect.getsource(main.detect_pii)
idx1 = src.find("account_number")
with open("pii_account_check.txt", "w", encoding="utf-8") as out:
    out.write(src[max(0,idx1-200):idx1+100])

print("DONE")