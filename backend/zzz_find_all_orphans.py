import main

with open("zzz_all_endpoints.txt", "w") as f:
    for r in main.app.routes:
        if hasattr(r, 'path') and hasattr(r, 'methods') and 'POST' in (r.methods or []):
            f.write(r.path + "\n")

print("DONE")