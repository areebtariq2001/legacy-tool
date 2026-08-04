import main
import inspect

src1 = inspect.getsource(main.generate_documentation)
src2 = inspect.getsource(main.generate_test_scenarios)
src3 = inspect.getsource(main.extract_business_rules)

print("generate_documentation uses call_ai_provider:", "call_ai_provider(" in src1)
print("generate_documentation has delimiters:", "BEGIN CODE" in src1)
print("generate_test_scenarios uses call_ai_provider:", "call_ai_provider(" in src2)
print("generate_test_scenarios has delimiters:", "BEGIN CODE" in src2)
print("extract_business_rules uses call_ai_provider:", "call_ai_provider(" in src3)
print("extract_business_rules has delimiters:", "BEGIN CODE" in src3)