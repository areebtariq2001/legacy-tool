import main
import inspect

src = inspect.getsource(main.detect_pii)
with open("detect_pii_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))