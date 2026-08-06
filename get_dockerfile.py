import main
import inspect

src = inspect.getsource(main.generate_dockerfile)
with open("dockerfile_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))