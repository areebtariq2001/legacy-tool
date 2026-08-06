import main
import inspect

src = inspect.getsource(main.detect_banking_patterns)
with open("banking_current_check.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")