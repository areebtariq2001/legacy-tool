import main
code = "IDENTIFICATION DIVISION." + chr(10) + "DATA DIVISION." + chr(10) + "WORKING-STORAGE SECTION." + chr(10) + '01 WS-ACCOUNT-ID PIC X(10) VALUE "12345".' + chr(10) + "01 WS-BALANCE PIC 9(7)V99 VALUE 0." + chr(10) + "PROCEDURE DIVISION." + chr(10) + 'DISPLAY "Starting program".' + chr(10) + 'MOVE "67890" TO WS-ACCOUNT-ID.' + chr(10) + "STOP RUN."
r = main.migrate_cobol(code)
print(r.get("changes"))
print("---")
print(r.get("migrated_code"))
