import main
import inspect

src = inspect.getsource(main.detect_banking_patterns)
with open("detect_banking_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))