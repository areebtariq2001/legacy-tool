import main
import inspect

with open("zzz_more_sigs.txt", "w") as f:
    for name in dir(main):
        obj = getattr(main, name)
        if callable(obj) and 'endpoint' in name.lower():
            try:
                sig = inspect.signature(obj)
                f.write(name + str(sig) + "\n")
            except:
                pass

print("DONE")