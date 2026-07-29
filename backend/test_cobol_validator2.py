import main
r2 = main.migrate_cobol("IDENTIFICATION DIVISION.\nPROGRAM-ID. TEST.\nPROCEDURE DIVISION.\nDISPLAY 'HI'.")
print("COBOL validation:", r2.get("validation"))