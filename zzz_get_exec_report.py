import main
import inspect

src = inspect.getsource(main.generate_executive_report)
with open("zzz_exec_report.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))