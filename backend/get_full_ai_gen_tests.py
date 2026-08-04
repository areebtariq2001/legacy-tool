import main
import inspect

src = inspect.getsource(main.ai_generate_tests)
with open("full_ai_gen_tests.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")