import main
import inspect

src = inspect.getsource(main.call_ai_provider)
with open("call_ai_provider_output.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")