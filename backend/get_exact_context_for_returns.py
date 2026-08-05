import main
import inspect

src_php = inspect.getsource(main.analyze_php)
src_cobol = inspect.getsource(main.analyze_cobol)

with open("exact_context_output.txt", "w", encoding="utf-8") as out:
    out.write("=== PHP last 400 chars ===\n")
    out.write(src_php[-400:])
    out.write("\n\n=== COBOL last 400 chars ===\n")
    out.write(src_cobol[-400:])

print("DONE")