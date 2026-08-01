import main

test_code = """       IDENTIFICATION DIVISION.
       PROCEDURE DIVISION.
           PERFORM PROCESS-ITEM UNTIL WS-DONE = "Y" WITH TEST AFTER.
           STOP RUN."""

result = main.migrate_cobol(test_code)
print("Migrated code:")
print(result["migrated_code"])
print()
print("Genuinely-valid-Python syntax check:")
try:
    compile(result["migrated_code"], "<test>", "exec")
    print("VALID")
except SyntaxError as e:
    print("SYNTAX ERROR:", e)