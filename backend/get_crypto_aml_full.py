import main
import inspect

src1 = inspect.getsource(main.scan_crypto)
src2 = inspect.getsource(main.extract_aml_kyc)

with open("crypto_aml_full.txt", "w", encoding="utf-8") as out:
    out.write("=== scan_crypto ===\n" + src1)
    out.write("\n\n=== extract_aml_kyc ===\n" + src2)

print("DONE")