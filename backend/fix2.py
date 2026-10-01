main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

results = {}

old2 = '"summary": (str(len(findings)) + " mainframe-specific construct reference(s) found across " + str(len(top_categories)) + " categories - showing first " + str(len(findings)) + "."),'
new2 = '"total_matches": sum(counts.values()), "summary": (str(sum(counts.values())) + " mainframe-specific construct reference(s) found across " + str(len(counts)) + " categories - showing first " + str(len(findings)) + " individual match(es)."),'
results["2_cobol_dialect"] = content.count(old2)
content = content.replace(old2, new2, 1)

old3 = '"summary": (str(len(findings)) + " potential CBS/Core-Banking integration-point reference(s) found across " + str(len(top_categories)) + " categories - showing first " + str(len(findings)) + "."),'
new3 = '"total_matches": sum(counts.values()), "summary": (str(sum(counts.values())) + " potential CBS/Core-Banking integration-point reference(s) found across " + str(len(counts)) + " categories - showing first " + str(len(findings)) + " individual match(es)."),'
results["3_cbs_integration"] = content.count(old3)
content = content.replace(old3, new3, 1)

with open(main_path, "w", encoding="utf-8") as f:
    f.write(content)

for k, v in results.items():
    print(k, ":", v)
print("FIX2-DONE")