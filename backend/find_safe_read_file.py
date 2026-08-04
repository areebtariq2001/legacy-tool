import main
import inspect

src = inspect.getsource(main.safe_read_file)
with open("safe_read_file_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")