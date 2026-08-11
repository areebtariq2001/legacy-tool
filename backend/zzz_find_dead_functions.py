import main
import inspect

# Get all module-level functions
all_funcs = [name for name, obj in vars(main).items() if inspect.isfunction(obj) and obj.__module__ == 'main']

# Get all endpoint-called function names by checking route source
route_calls = set()
for r in main.app.routes:
    if hasattr(r, 'endpoint'):
        try:
            src = inspect.getsource(r.endpoint)
            route_calls.add(src)
        except:
            pass

all_route_source = " ".join(route_calls)

orphaned = []
for fname in all_funcs:
    if fname.startswith("_"):
        continue
    if fname in ("app",):
        continue
    if fname not in all_route_source:
        orphaned.append(fname)

with open("zzz_dead_functions.txt", "w") as f:
    for fn in orphaned:
        f.write(fn + "\n")

print("DONE - total functions:", len(all_funcs), "potentially orphaned:", len(orphaned))