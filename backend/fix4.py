main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

old = '"total_findings": len(findings), "category_counts": counts, "summary": (str(len(findings)) + " potential CBS/Core-Banking integration-point reference(s) found across " + str(len(counts)) + " categories - this is an inventory to help plan migration scope, not an automated migration.") if findings else "No T24/Finacle/Misys/SYMBOL core-banking-system integration references detected in this file."'
new = '"total_findings": sum(counts.values()), "findings_shown": len(findings), "category_counts": counts, "summary": (str(sum(counts.values())) + " potential CBS/Core-Banking integration-point reference(s) found across " + str(len(counts)) + " categories (showing first " + str(len(findings)) + " individual match(es)) - this is an inventory to help plan migration scope, not an automated migration.") if findings else "No T24/Finacle/Misys/SYMBOL core-banking-system integration references detected in this file."'

count = content.count(old)
print("Occurrences found:", count)
if count == 1:
    content = content.replace(old, new, 1)
    with open(main_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("FIX4-CBS-INTEGRATION-DONE")
else:
    print("FAILED - count was:", count)