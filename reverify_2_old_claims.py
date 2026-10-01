main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("reverify_2_old_claims_result.txt", "w", encoding="utf-8") as out:
    idx1 = content.find("No executable code was found to migrate")
    out.write("=== CLAIM-1: empty-code return + prompt=( ===\n")
    out.write(content[idx1:idx1+280] + chr(10) + chr(10))

    idx2 = content.find("for pattern, msg in review_rules")
    out.write("=== CLAIM-2: migrate_php review_rules loop ===\n")
    out.write(content[idx2:idx2+140])
print("REVERIFY-2-OLD-CLAIMS-DONE")