main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old2 = '"total_findings": len(findings), "category_counts": counts, "summary": (str(len(findings)) + " mainframe-specific construct reference(s) found across " + str(len(counts)) + " categories - this is an inventory to help plan migration scope, not an automated migration.") if findings else "No CICS/IMS/JCL/VSAM/MQ/Copybook references detected in this file."'
new2 = '"total_findings": sum(counts.values()), "findings_shown": len(findings), "category_counts": counts, "summary": (str(sum(counts.values())) + " mainframe-specific construct reference(s) found across " + str(len(counts)) + " categories (showing first " + str(len(findings)) + " individual match(es)) - this is an inventory to help plan migration scope, not an automated migration.") if findings else "No CICS/IMS/JCL/VSAM/MQ/Copybook references detected in this file."'
results["2_cobol_dialect"] = content.count(old2)
content = content.replace(old2, new2, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIX3-DONE")