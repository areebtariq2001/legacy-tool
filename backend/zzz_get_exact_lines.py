with open("main.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

keywords = ["score=", "risk=", "recs=", "tables=", "libs=", "layers=",
            "AI-native check failed", "Risk prediction failed", "CI/CD recommendations failed",
            "DB schema analysis failed", "API dependency mapping failed", "Architecture generation failed"]

with open("zzz_exact_lines_out.txt", "w", encoding="utf-8") as out:
    for i, line in enumerate(lines):
        for kw in keywords:
            if kw in line:
                out.write(str(i+1) + ": " + line)

print("DONE")