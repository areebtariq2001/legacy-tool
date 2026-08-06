import main
import inspect

src = inspect.getsource(main.generate_test_scenarios)
with open("test_scenarios_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))