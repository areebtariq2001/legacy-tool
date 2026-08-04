import main
import inspect

src1 = inspect.getsource(main.generate_documentation)
src2 = inspect.getsource(main.generate_test_scenarios)
src3 = inspect.getsource(main.extract_business_rules)

with open("3_funcs_full.txt", "w", encoding="utf-8") as out:
    out.write("=== generate_documentation ===\n" + src1)
    out.write("\n\n=== generate_test_scenarios ===\n" + src2)
    out.write("\n\n=== extract_business_rules ===\n" + src3)

print("DONE")