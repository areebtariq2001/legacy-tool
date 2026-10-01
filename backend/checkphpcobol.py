main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("checkphpcobol_result.txt", "w", encoding="utf-8") as out:
    out.write("=== remaining 'confidence_score': 90 or ]=90 or ]=95 occurrences ===\n")
    out.write("count-90-colon: " + str(content.count('"confidence_score": 90')) + chr(10))
    out.write("count-90-bracket: " + str(content.count('"confidence_score"] = 90')) + chr(10))
    out.write("count-95-bracket: " + str(content.count('"confidence_score"] = 95')) + chr(10))
    out.write("count-Low-confidence-fix-applied: " + str(content.count("Low confidence - AI failed")) + chr(10) + chr(10))

    out.write("=== def migrate_php fallback section ===\n")
    idx = content.find("def migrate_php")
    idx_end = content.find("\ndef ", idx+20)
    body = content[idx:idx_end]
    ridx = body.find("except")
    out.write(body[max(0,ridx-50):ridx+500] if ridx != -1 else "no-except-in-migrate_php")
print("CHECKPHPCOBOL-DONE")