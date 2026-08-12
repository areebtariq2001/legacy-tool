import main
import inspect

src = inspect.getsource(main._check_admin_auth)
with open("zzz_admin_auth_out.txt", "w", encoding="utf-8") as out:
    out.write(src)

print("DONE")