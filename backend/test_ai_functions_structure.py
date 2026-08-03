import main
import inspect

src1 = inspect.getsource(main.ai_suggest)
src2 = inspect.getsource(main.ai_explain)

print("ai_suggest uses call_ai_provider:", "call_ai_provider(" in src1)
print("ai_suggest has truncation:", "truncated" in src1)
print("ai_suggest has delimiters:", "BEGIN CODE" in src1)
print("ai_suggest has error-check:", "AI_ERROR" in src1 and "error" in src1)
print()
print("ai_explain uses call_ai_provider:", "call_ai_provider(" in src2)
print("ai_explain has truncation:", "truncated" in src2)
print("ai_explain has delimiters:", "BEGIN CODE" in src2)