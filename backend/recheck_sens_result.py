main_path = r"C:\Users\dell\Desktop\legacy-migration-tool\backend\main.py"

with open(main_path, "r", encoding="utf-8") as f:
    content = f.read()

c_old_pass = content.count("except Exception:\n        pass")
c_new_fix = content.count("sub-check failed")
c_old_marker = content.count("_sens_result = scan_sensitive_data(source)")

with open("recheck_sens_result_result.txt", "w", encoding="utf-8") as out:
    out.write("Genuinely-remaining-'except-Exception:-pass'-count: " + str(c_old_pass) + chr(10))
    out.write("Genuinely-'sub-check-failed'-fix-text-count: " + str(c_new_fix) + chr(10))
    out.write("Genuinely-'_sens_result-=-scan_sensitive_data'-count: " + str(c_old_marker))
print("RECHECK-SENS-RESULT-DONE")