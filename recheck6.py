main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

with open("recheck6_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-'findings_full'-total-occurrences (should be 9+ now, was 0 before all fixes): " + str(content.count("findings_full")) + chr(10))
    out.write("Genuinely-'findings_truncated'-total-occurrences: " + str(content.count("findings_truncated")) + chr(10))
    out.write("Genuinely-scan_cbs_integration_points-has-sum(counts.values()): " + chr(10))
    idx = content.find("def scan_cbs_integration_points")
    idx_end = content.find("\ndef ", idx+20)
    body = content[idx:idx_end]
    out.write("  -> 'sum(counts.values())' present: " + str("sum(counts.values())" in body) + chr(10))
    out.write("Genuinely-process_github_webhook-has-total_changed_files_detected: " + chr(10))
    idx2 = content.find("def process_github_webhook")
    idx2_end = content.find("\ndef ", idx2+20)
    body2 = content[idx2:idx2_end]
    out.write("  -> 'total_changed_files_detected' present: " + str("total_changed_files_detected" in body2) + chr(10))
    out.write("Genuinely-scan_entropy_secrets-high_count-uses-findings_full: " + chr(10))
    idx3 = content.find("def scan_entropy_secrets")
    idx3_end = content.find("\ndef ", idx3+20)
    body3 = content[idx3:idx3_end]
    out.write("  -> 'sum(1 for f in findings_full if f[\"confidence\"]' present: " + str('sum(1 for f in findings_full if f["confidence"]' in body3))
print("RECHECK6-DONE")