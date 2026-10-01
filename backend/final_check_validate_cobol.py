main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

c1 = content.count("validate_cobol")
c2 = content.count("validate_migrated_cobol_output")

with open("final_check_validate_cobol_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-old-name-remaining (should-be-0): " + str(c1) + chr(10))
    out.write("Genuinely-new-name-count (should-be-2): " + str(c2))
print("FINAL-CHECK-VALIDATE-COBOL-DONE")