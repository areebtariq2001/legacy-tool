import main

test_code = """       IDENTIFICATION DIVISION.
       PROGRAM-ID. TEST.
       PROCEDURE DIVISION.
           COMPUTE WS-INTEREST = WS-PRINCIPAL * WS-RATE / 100.
           STOP RUN."""

result = main.migrate_cobol(test_code)
print("Changes:")
for c in result["changes"]:
    print(" -", c[:100])