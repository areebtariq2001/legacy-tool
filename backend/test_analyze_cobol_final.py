import main

# Test Bug-2: word boundary (should NOT match "EPIC 9000" as "PIC 9")
test1 = "* EPIC 9000 SYSTEM COMMENT"
result1 = main.analyze_cobol(test1)
print("False-positive test (EPIC-9000):", result1["issues"])

# Test genuine PERFORM variants (Bug-9)
test2 = """PERFORM UNTIL WS-DONE = "Y".
PERFORM PROCESS-RECORD."""
result2 = main.analyze_cobol(test2)
print("PERFORM variants:", result2["issues"])

# Test new missing patterns (Bug-5)
test3 = "01 WS-REC REDEFINES WS-OLD-REC. EXEC SQL SELECT * END-EXEC."
result3 = main.analyze_cobol(test3)
print("New patterns (REDEFINES/EXEC SQL):", result3["issues"])