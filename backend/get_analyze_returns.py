import main
import inspect

src1 = inspect.getsource(main.analyze_java)
src2 = inspect.getsource(main.analyze_php)
src3 = inspect.getsource(main.analyze_cobol)

with open("analyze_returns.txt", "w", encoding="utf-8") as out:
    out.write("=== analyze_java RETURN ===\n")
    idx = src1.rfind("return")
    out.write(src1[idx:idx+300])
    out.write("\n\n=== analyze_php RETURN ===\n")
    idx = src2.rfind("return")
    out.write(src2[idx:idx+300])
    out.write("\n\n=== analyze_cobol RETURN ===\n")
    idx = src3.rfind("return")
    out.write(src3[idx:idx+300])

print("DONE")