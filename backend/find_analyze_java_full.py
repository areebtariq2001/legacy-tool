import main
import inspect

java_src = inspect.getsource(main.analyze_java)
cobol_src = inspect.getsource(main.analyze_cobol)

with open("full_lang_funcs.txt", "w", encoding="utf-8") as out:
    out.write("=== analyze_java ===\n")
    out.write(java_src)
    out.write("\n\n=== analyze_cobol ===\n")
    out.write(cobol_src)

print("DONE")