import main
import inspect

src = inspect.getsource(main.scan_crypto)
with open("crypto_current_check.txt", "w", encoding="utf-8") as out:
    out.write("Uses CRYPTO_PATTERNS_COMPILED: " + str("CRYPTO_PATTERNS_COMPILED" in src) + "\n")
    out.write("Has lines field: " + str('"lines"' in src) + "\n\n")
    out.write(src)

with open("crypto_patterns_list.txt", "w", encoding="utf-8") as out2:
    for p, label, sev, rec in main.CRYPTO_PATTERNS:
        out2.write(repr(p) + " | " + label + " | " + sev + "\n")

print("DONE")