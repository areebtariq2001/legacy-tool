with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

patterns_to_check = [
    '"score=" + str(',
    '"risk=" + str(',
    '"recs=" + str(',
    '"tables=" + str(',
    '"libs=" + str(',
    '"layers=" + str(',
    '"AI-native check failed safely: " + str(e)',
    '"Risk prediction failed safely: " + str(e)',
    '"CI/CD recommendations failed safely: " + str(e)',
    '"DB schema analysis failed safely: " + str(e)',
    '"API dependency mapping failed safely: " + str(e)',
    '"Architecture generation failed safely: " + str(e)',
]

with open("zzz_6endpoints_check.txt", "w") as out:
    for p in patterns_to_check:
        count = content.count(p)
        out.write(f"{count} : {p}\n")

print("DONE")