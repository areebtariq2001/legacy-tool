import main
r1 = main.migrate_php('<?php function test() { echo "hi"; } ?>')
print("PHP validation:", r1.get("validation"))
r2 = main.migrate_cobol("IDENTIFICATION DIVISION.\nPROGRAM-ID. TEST.\nPROCEDURE DIVISION.\nDISPLAY 'HI'.")
print("COBOL validation:", r2.get("validation"))