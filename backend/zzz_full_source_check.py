import main
import inspect

src = inspect.getsource(main.analyze_call_graph)
with open("zzz_source_check.txt", "w", encoding="utf-8") as f:
    f.write("LENGTH: " + str(len(src)) + "\n")
    f.write("=" * 40 + "\n")
    f.write(src)

print("DONE")