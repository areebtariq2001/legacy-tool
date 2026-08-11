import main
import inspect

src = inspect.getsource(main.scan_crypto)
with open("zzz_scan_crypto_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))