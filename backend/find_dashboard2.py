with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

with open("dashboard_output2.txt", "w", encoding="utf-8") as out:
    if "migration_dashboard_endpoint" in content:
        out.write("FOUND: migration_dashboard_endpoint\n")
    else:
        out.write("NOT FOUND: migration_dashboard_endpoint\n")
    if "async def db_debug_endpoint" in content:
        out.write("FOUND: db_debug_endpoint\n")

print("DONE")