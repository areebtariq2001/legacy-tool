import main

test1 = "print >>sys.stderr, chr(34) + chr(101) + chr(114) + chr(114) + chr(111) + chr(114) + chr(34)"
r1 = main.migrate_code(test1)
with open("chevron_test.txt", "w", encoding="utf-8") as out:
    out.write("CHEVRON:\n" + r1["migrated_code"] + "\nVALID: " + str(r1.get("migration_validity")))

test2 = "print " + chr(34) + "a" + chr(34) + "; x = 5"
r2 = main.migrate_code(test2)
with open("multistmt_test.txt", "w", encoding="utf-8") as out:
    out.write("MULTISTMT:\n" + r2["migrated_code"] + "\nVALID: " + str(r2.get("migration_validity")))

print("DONE genuinely")
