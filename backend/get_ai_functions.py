import main
import inspect

src1 = inspect.getsource(main.ai_suggest)
src2 = inspect.getsource(main.ai_explain)

with open("ai_functions_output.txt", "w", encoding="utf-8") as out:
    out.write("=== ai_suggest ===\n")
    out.write(src1)
    out.write("\n\n=== ai_explain ===\n")
    out.write(src2)

print("DONE")