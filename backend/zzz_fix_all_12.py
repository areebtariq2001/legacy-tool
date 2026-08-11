with open("main.py", "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ('write_audit_log("ai-native-readiness", file.filename, "score=" + str(result.get("ai_native_score", 0)))',
     'write_audit_log("ai-native-readiness", file.filename, f"score={result.get(\'ai_native_score\', 0)}")'),
    ('return {"filename": file.filename, "error": "AI-native check failed safely: " + str(e)}',
     'return {"filename": file.filename, "error": f"AI-native check failed safely: {e}"}'),
    ('write_audit_log("predict-risk", file.filename, "risk=" + str(result.get("migration_risk", 0)))',
     'write_audit_log("predict-risk", file.filename, f"risk={result.get(\'migration_risk\', 0)}")'),
    ('return {"filename": file.filename, "error": "Risk prediction failed safely: " + str(e)}',
     'return {"filename": file.filename, "error": f"Risk prediction failed safely: {e}"}'),
    ('write_audit_log("cicd-recommendations", file.filename, "recs=" + str(len(result.get("cicd_recommendations", []))))',
     'write_audit_log("cicd-recommendations", file.filename, f"recs={len(result.get(\'cicd_recommendations\', []))}")'),
    ('return {"filename": file.filename, "error": "CI/CD recommendations failed safely: " + str(e)}',
     'return {"filename": file.filename, "error": f"CI/CD recommendations failed safely: {e}"}'),
    ('write_audit_log("analyze-db-schema", file.filename, "tables=" + str(len(result.get("tables", []))))',
     'write_audit_log("analyze-db-schema", file.filename, f"tables={len(result.get(\'tables\', []))}")'),
    ('return {"filename": file.filename, "error": "DB schema analysis failed safely: " + str(e)}',
     'return {"filename": file.filename, "error": f"DB schema analysis failed safely: {e}"}'),
    ('write_audit_log("map-api-dependencies", file.filename, "libs=" + str(len(result.get("http_libraries", []))))',
     'write_audit_log("map-api-dependencies", file.filename, f"libs={len(result.get(\'http_libraries\', []))}")'),
    ('return {"filename": file.filename, "error": "API dependency mapping failed safely: " + str(e)}',
     'return {"filename": file.filename, "error": f"API dependency mapping failed safely: {e}"}'),
    ('write_audit_log("generate-architecture", file.filename, "layers=" + str(len(result.get("architecture_layers", []))))',
     'write_audit_log("generate-architecture", file.filename, f"layers={len(result.get(\'architecture_layers\', []))}")'),
    ('return {"filename": file.filename, "error": "Architecture generation failed safely: " + str(e)}',
     'return {"filename": file.filename, "error": f"Architecture generation failed safely: {e}"}'),
]

total_patched = 0
with open("zzz_fix12_log.txt", "w") as log:
    for old, new in replacements:
        count = content.count(old)
        log.write(str(count) + " : " + old[:60] + "\n")
        if count == 1:
            content = content.replace(old, new, 1)
            total_patched += 1

with open("main.py", "w", encoding="utf-8") as f:
    f.write(content)

print("DONE - total patched:", total_patched, "of", len(replacements))