import main
import inspect

src = inspect.getsource(main.extract_aml_kyc)
with open("aml_kyc_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

with open("aml_kyc_patterns.txt", "w", encoding="utf-8") as out2:
    for p, label, cat, note in main.AML_KYC_PATTERNS:
        out2.write(repr(p) + " | " + label + " | " + cat + "\n")

print("DONE")