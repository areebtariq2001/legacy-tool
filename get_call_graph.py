import main
import inspect

src = inspect.getsource(main.analyze_call_graph)
with open("call_graph_full.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))