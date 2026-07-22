import main
code = "IDENTIFICATION DIVISION." + chr(10) + "PROCEDURE DIVISION." + chr(10) + "MAIN-LOGIC." + chr(10) + '    DISPLAY "start".' + chr(10) + "GET-ACCOUNT-BALANCE." + chr(10) + '    DISPLAY "balance".' + chr(10) + "CHECK-TRANSACTION." + chr(10) + '    DISPLAY "check".' + chr(10) + "END-PROGRAM." + chr(10) + "    STOP RUN."
r = main.analyze_impact(code, "test.cbl")
print(r.get("impact_summary"))
