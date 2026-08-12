import main
import inspect

src = inspect.getsource(main.run_sandboxed_migration_test)
with open("zzz_sandbox_out.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE - length:", len(src))