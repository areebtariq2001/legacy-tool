import main
code = open("C:/Users/dell/Desktop/legacybank.cbl").read()
r = main.migrate_cobol(code)
with open("migrate_output.txt", "w") as f:
    f.write(r.get("migrated_code"))
print("saved to migrate_output.txt")