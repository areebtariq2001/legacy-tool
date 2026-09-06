import main
import inspect

funcs = ["check_audit_maker_checker", "check_cnic_validation_quality", "check_structuring_patterns",
         "check_ntn_strn_validation_quality", "check_unusual_hours_flag", "check_geo_anomaly_detection",
         "check_high_value_threshold"]

with open("audit_result.txt", "w", encoding="utf-8") as out:
    for fname in funcs:
        src = inspect.getsource(getattr(main, fname))
        return_lines = [l.strip() for l in src.split(chr(10)) if l.strip().startswith("return {") and "total_findings" not in l]
        out.write(fname + ": " + str(len(return_lines)) + " return(s)-missing-total_findings" + chr(10))
        for rl in return_lines:
            out.write("  -> " + rl[:150] + chr(10))
print("AUDIT-ALL-DONE")