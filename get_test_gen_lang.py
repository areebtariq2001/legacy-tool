import main
import inspect

src1 = inspect.getsource(main.ai_generate_tests)
src2 = inspect.getsource(main.detect_language)

with open("test_gen_lang_output.txt", "w", encoding="utf-8") as out:
    out.write("=== ai_generate_tests (length: " + str(len(src1)) + ") ===\n")
    out.write(src1[:800])
    out.write("\n\n=== detect_language ===\n")
    out.write(src2)

print("DONE")